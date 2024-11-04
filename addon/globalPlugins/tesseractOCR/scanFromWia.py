#-*- coding: utf-8 -*-
# Routines to scan and manage WIA scanners
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Thanks to Rainer <0049rob@googlemail.com> by initial code and ChatGPT by some hints, especially in setting scanner parameters and listing available scanners...
# Copyright (C) 2023-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# Import the necessary modules.
from .runInThread import *
from .vars import *
from .configPanel import *
import comtypes.client

# To start the translation process
addonHandler.initTranslation()

# Global variable
jpgFilePath = ""
scan_thread = None

# Function to get connected scanners via WIA
def getConnectedScanners():
	# Fetches the list of connected scanners via WIA.
	d = comtypes.client.CreateObject("WIA.DeviceManager")
	# Check if there are connected scanners
	if not d.DeviceInfos.count:
		ui.message(_("No scanner found. Please check the device connection."))
		return []
	# Returns a list of all connected scanners' names
	scanners = [d.DeviceInfos[i+1].Properties["Name"].Value for i in range(d.DeviceInfos.count)]
	return scanners

# Function to allow the user to select a scanner if more than one is available
def selectScanner():
	# Displays a dialog for the user to select the scanner if more than one is available.
	scanners = getConnectedScanners()
	if not scanners:
		return None
	# If there is only one scanner, use it directly
	if len(scanners) == 1:
		return scanners[0]
	# If more than one scanner is found, display a list for the user to choose from
	dialog = wx.SingleChoiceDialog(None, _("Select the scanner to use:"), _("Available Scanners"), scanners)
	if dialog.ShowModal() == wx.ID_OK:
		selectedScanner = dialog.GetStringSelection()
		dialog.Destroy()
		return selectedScanner
	else:
		dialog.Destroy()
		return None

# Thread class for the scanning process
class ScanThread(threading.Thread):
	def __init__(self, scanner):
		super(ScanThread, self).__init__()
		self.scanner = scanner
		self._stop_event = threading.Event()

	def run(self):
		# Starts the scanning process for multiple pages using the same scanner configuration.
		num = 1
		while not self._stop_event.is_set():
			global jpgFilePath
			jpgFilePath = os.path.join(PLUGIN_DIR, f"images/ocr{num:03d}.jpg")
			# Perform the scan using the already configured scanner
			if self.scanPage(self.scanner, jpgFilePath):
				# Ask if the user wants to scan another page
				if wx.MessageBox(_("Do you want to scan one more page?"), "TesseractOCR", wx.YES_NO | wx.ICON_QUESTION) == wx.NO:
					break
				num += 1
			else:
				break

	def scanPage(self, scanner, jpgFilePath):
		"""Scans a single page using the configured scanner."""
		try:
			# Check _stop_event before starting the scan
			if self._stop_event.is_set():
				return False
			item = scanner.Items(1)
			# Transfer image and save as JPG
			image = item.Transfer(comtypes.gen.WIA.wiaFormatJPEG)
			image.SaveFile(jpgFilePath)

			# Check _stop_event after the scan
			if self._stop_event.is_set():
				return False

			return True
		except comtypes.COMError as e:
			ui.message(_("Error during scanning: {}").format(e))
			return False

	def stop(self):
		# Signal to stop the scanning process.
		self._stop_event.set()

def configureScanner(scannerName):
	# Configures the selected scanner with the necessary settings for resolution, color, and scan area.
	d = comtypes.client.CreateObject("WIA.DeviceManager")
	for i in range(d.DeviceInfos.count):
		if d.DeviceInfos[i+1].Properties["Name"].Value == scannerName:
			scanner = d.DeviceInfos[i+1].Connect()
			# Set scanner settings (once per scanning session)
			item = scanner.Items(1)

			# Scanner settings (resolution, color, etc.)
			# 1 = Color, 2 = Grayscale, 4 = Black and White
			item.Properties("6146").Value = 2  # Grayscale
			# Set DPI (horizontal and vertical resolution)
			item.Properties("6147").Value = DPI
			item.Properties("6148").Value = DPI
			# Set the scanning area (full page)
			item.Properties("6149").Value = item.Properties("6149").SubTypeMin  # Horizontal start
			item.Properties("6150").Value = item.Properties("6150").SubTypeMin  # Vertical start
			item.Properties("6151").Value = item.Properties("6151").SubTypeMax  # Maximum width
			item.Properties("6152").Value = item.Properties("6152").SubTypeMax  # Maximum height

			return scanner  # Return the configured scanner
	ui.message(_("Scanner not found."))
	return None

def startScanningProcess():
	# Starts the scanning process, allowing the user to select the scanner if necessary.
	global scan_thread
	selectedScanner = selectScanner()
	if not selectedScanner:
		ui.message(_("No scanner was selected or found."))
		return
	# Configure the selected scanner only once
	configuredScanner = configureScanner(selectedScanner)
	if not configuredScanner:
		return
	# Start scanning in a new thread using the configured scanner
	scan_thread = ScanThread(configuredScanner)
	scan_thread.start()
	scan_thread.join()

class ScanFromWia():
	def run(self):
		# Start the scanning process by selecting and configuring the scanner
		startScanningProcess()

#-*- coding: utf-8 -*-
# Routines to digitalize and manage WIA scanners
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Thanks to Rainer <0049rob@googlemail.com> by initial code and to ChatGPT by some hints, specially im setting scanner parameters and listing available scanners...
# Copyright (C) 2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
from .runInThread import *
from .vars import *
from .configPanel import *
import comtypes.client
import time

# To start the translation process
addonHandler.initTranslation()

endTask = False
jpgFilePath = ""


class ScanThread(threading.Thread):
	def run(self):
		from .vars import DPI, scanner
		global endTask, num, jpgFilePath
		num = ""
		n = 1
		# Create routine for multiple scannings
		while n <= 999:
			num = "{:03d}".format(n)
			jpgFilePath = os.path.join(PLUGIN_DIR, "images", "ocr" + num + ".jpg")
			# Create WIA connection
			d = comtypes.client.CreateObject("WIA.DeviceManager")
			# Check if WIA devices are present
			if not d.DeviceInfos.count:
				# Translators: Reported when no WIA devices are available
				ui.message(_("No WIA devices available. Please check if your scanner is conected and if is WIA compatible"))
				return
			# Connect with scanner devices
			from .configPanel import scanner
			# Getting the selected device in config or the first available...
			DEV = WIAList.index(scanner) + 1
			s = d.DeviceInfos(str(DEV)).Connect
			item = s().Items(1)
			# Set scanner properties
			# 1 = Color, 2 = Grayscale, 4 = Black and White
			item.Properties("6146").Value = 2
			# Resolution in DPI
			item.Properties("6147").Value = DPI
			# Digitalize one page from scanner
			try:
				image = item.Transfer(comtypes.gen.WIA.wiaFormatJPEG)
			except comtypes.COMError as e:
				if str(e).startswith("(-2145320954,"):
					pass
				else:
					raise e
				image.SaveFile(jpgFilePath)
				if endTask == False:
					# Check if are more pages to scan...
					if gui.messageBox(_("Do you want to scan one more page?"), "TesseractOCR", style=wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
						# More pages to scan...
						n += 1
					else:
						# No more pages to scan...
						endTask = True
						n = 1000
			else:
				image.SaveFile(jpgFilePath)
				if endTask == False:
					# Check if are more pages to scan...
					if gui.messageBox(_("Do you want to scan one more page?"), "TesseractOCR", style=wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
						# More pages to scan...
						n += 1
					else:
						# No more pages to scan...
						endTask = True
						n = 1000


class ScanFromWia():
	def run(self):
		global endTask
		endTask = False
		DevMan = comtypes.client.CreateObject("WIA.DeviceManager")
		scan = ScanThread()
		scan.start()
		scan.join()

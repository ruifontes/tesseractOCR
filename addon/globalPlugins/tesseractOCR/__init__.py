#-*- coding: utf-8 -*-
# Main file for Tesseract OCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Thanks to ChatGPT for some help!
# Copyright (C) 2020-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
from .scanFromWia import *
import sys
import subprocess
import api
import ctypes
import controlTypes
# For compatibility with old NVDA versions
if hasattr(controlTypes, "Role"):
	for r in controlTypes.Role: setattr(controlTypes, r.__str__().replace("Role.", "ROLE_"), r)
else:
	setattr(controlTypes, "Role", type('Enum', (), dict([(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
if hasattr(controlTypes, "State"):
	for r in controlTypes.State: setattr(controlTypes, r.__str__().replace("State.", "STATE_"), r)
else:
	setattr(controlTypes, "State", type('Enum', (), dict([(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))

import comtypes.client
from comtypes.client import CreateObject as COMCreate
import shutil
import psutil
from scriptHandler import script
import languageHandler

# To start the translation process
addonHandler.initTranslation()

# Place tessdata in PYTHONPATH
sys.path.append(os.path.join(PLUGIN_DIR, "tesseract", "tessdata"))
del sys.path[-1]

# Determine the maximum number of cores of the system
num_cores = psutil.cpu_count(logical=False)
# Tesseract do not manage well more than 4 cores... so, set at half of cores existent, but not more than 4.
max_cores = min(4, int(num_cores / 2))
# Set the maximum number of cores for Tesseract
os.environ["OMP_THREAD_LIMIT"] = str(max_cores)

# Global vars
docPath = ""
pwd = ""
jpgFilePath = ""
scanning = False

initConfiguration()

if globalVars.appArgs.secure:
	# Override the global plugin to disable it.
	GlobalPlugin = globalPluginHandler.GlobalPlugin


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		# Call of the constructor of the parent class.
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		# Adding a NVDA configurations section
		gui.NVDASettingsDialog.categoryClasses.append(OCRSettingsPanel)
		self._thread = None

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(OCRSettingsPanel)

	def deleteFiles(self):
		# Delete the temporary images folder and create again
		shutil.rmtree(os.path.join(PLUGIN_DIR, "images"), ignore_errors=True)
		os.mkdir(os.path.join(PLUGIN_DIR, "images"))
		# Delete the temporary list file
		from .vars import listPath
		try:
			filePath = listPath[1:-1]
			os.remove(filePath)
		except FileNotFoundError:
			pass

	def getDocName(self):
		# getting file path and name
		# We check if we are in the Windows Explorer.
		fg = api.getForegroundObject()
		if fg.role != api.controlTypes.Role.PANE and fg.appModule.appName != "explorer":
			return
		shell = COMCreate("shell.application")
		# We go through the list of open Windows Explorers to find the one that has the focus.
		for window in shell.Windows():
			try:
				if window.hwnd and window.hwnd == fg.windowHandle:
					focusedItem=window.Document.FocusedItem
					break
			except:
				pass
		else:
			# loop exhausted
			desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
			docPath = '\"' + desktop_path + '\\' + api.getDesktopObject().objectWithFocus().name + '\"'
			return
		# Now that we have the current folder, we can explore the SelectedItems collection.
		targetFile= focusedItem.path
		docPath = '\"' + str(targetFile) + '\"'
		return docPath

	def get_documents_folder(self):
		# Get path of documents folder
		from ctypes import wintypes
		# Code of "Documents" folder
		CSIDL_PERSONAL = 5
		# The folder can be moved, so get the actual folder path
		SHGFP_TYPE_CURRENT = 0
		buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
		ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
		return buf.value

	def convertPDFToPNG(self):
		# Transform PDF files in PNG files, since PDF format is not accepted by Tesseract...
		global pwd
		from .vars import pdf2PNGPath, pngFilesPath
		from .configPanel import shouldAskPwd
		# Check if should ask for password
		shouldAskPwd = config.conf["tesseractOCR"]["askPassword"]
		if shouldAskPwd == True and pwd != "":
			command = "{} -r 300 -gray -upw {} {} {}".format(pdf2PNGPath, pwd, docPath, pngFilesPath)
		else:
			command = "{} -r 300 -gray {} {}".format(pdf2PNGPath, docPath, pngFilesPath)
		totalPages = "0"
		self.backgroundProcessing(command, totalPages, pngFilesPath)

	def createList(self, extension):
		try:
			self.conv.stop()
		except AttributeError:
			pass
		from .vars import listPath
		# Check the files created and list them in list.txt...
		items = os.listdir(os.path.join(PLUGIN_DIR, "images"))
		list = []
		# Get the files
		for name in items:
			if name.endswith(extension):
				list.append(os.path.join(PLUGIN_DIR, "images", name))
		if len(list) != 0:
			# We have files, so write the names in the list.txt file
			with open(listPath[1:-1], "w", encoding = "latin1") as f:
				for x in range(len(list)):
					f.write(list[x] + "\n")
				f.close()
			totalPages = len(list)
			if extension == ".jpg":
				# Check if it is necessary to detect paper orientation
				from .configPanel import shouldDetect
				if shouldDetect == True:
					self.checkOrieintation(listPath, totalPages)
				else:
					# Perform OCR to all files in the list.txt
					self.OCR_image_files(listPath, totalPages)
			else:
				# Perform OCR to all files in the list.txt
				self.OCR_image_files(listPath, totalPages)
		else:
			return

	def checkOrieintation(self, path, totalPages):
		from .vars import tesseractPath, pngFilesPath, shouldDetect
		from .scanFromWia import jpgFilePath
		# Removing the extension in order to use the file name as new file name with the osd extension
		jpgFilePath = "\"" + jpgFilePath[:-4] + "\""
		global pngFilesPath
		# digitalizing from scanner, so is better have auto-orientation of the text.., so lang = "osd"
		command = "{} {} {} --dpi 300 --psm 0 --oem 1 -c tessedit_do_invert=0 -l osd quiet".format(tesseractPath, path, jpgFilePath)
		self.backgroundProcessing(command, totalPages)
		with open(os.path.join(PLUGIN_DIR, "images", "ocr001.osd"), "r", encoding = "utf-8") as f:
			text = f.readlines()
			OrientationLine = text[1]
			if OrientationLine.endswith("270\n") is True:
				# Announce orientation and ask if should process OCR
				if gui.messageBox(_("Page is rotated to the right. Do you want to process the OCR?"), "TesseractOCR", style=wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
					# Perform OCR to all JPG files in the list.txt
					self.OCR_image_files(path, totalPages)
			elif OrientationLine.endswith("180\n") is True:
				# Announce orientation and ask if should process OCR
				if gui.messageBox(_("Page is upside down. Do you want to process the OCR?"), "TesseractOCR", style=wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
					# Perform OCR to all JPG files in the list.txt
					self.OCR_image_files(path, totalPages)
			elif OrientationLine.endswith("90\n") is True:
				# Announce orientation and ask if should process OCR
				if gui.messageBox(_("Page is rotated to the left. Do you want to process the OCR?"), "TesseractOCR", style=wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
					# Perform OCR to all JPG files in the list.txt
					self.OCR_image_files(path, totalPages)
			elif OrientationLine.endswith(" 0\n") is True:
				# Announce orientation and ask if should process OCR
				if gui.messageBox(_("Page is positioned correctly. Do you want to process the OCR?"), "TesseractOCR", style=wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
					# Perform OCR to all JPG files in the list.txt
					self.OCR_image_files(path, totalPages)
			else:
				return

	def OCR_image_files(self, path, totalPages):
		path = path
		from .vars import tesseractPath, pngFilesPath
		from .configPanel import lang, doc
		from .scanFromWia import jpgFilePath
		# Removing the extension in order to use the file name as new file name with the txt extension
		jpgFilePath = "\"" + jpgFilePath[:-4] + "\""
		global scanning, pngFilesPath
		self.ocr = runInThread.RepeatBeep(delay=2.0, beep=(300, 300), isRunning=None)
		self.ocr.start()
		# Perform OCR to the selected image file
		# Different command for scanned documents or files
		lang = "osd" + "+" + lang
		if scanning == True:
			# Thai language is writen without spaces, so it is necessary the parameter "preserve_interword_spaces=1"
			if "tha" in lang:
				command = "{} {} {} --dpi 300 --psm 1 --oem 1 -c preserve_interword_spaces=1 -l {}".format(tesseractPath, path, jpgFilePath, lang)
			else:
				command = "{} {} {} --dpi 300 --psm 1 --oem 1 -c tessedit_do_invert=0 -l {}".format(tesseractPath, path, jpgFilePath, lang)
			self.backgroundProcessing(command, totalPages, path)
			self.ocr.stop()
			self.creatTXTFromVariousTXT()
		else:
			# Thai language is writen without spaces, so it is necessary the parameter "preserve_interword_spaces=1"
			if "tha" in lang:
				command = "{} {} {} --dpi 300 --psm {} --oem 1 -c preserve_interword_spaces=1 -l {}".format(tesseractPath, path, pngFilesPath, doc, lang)
			else:
				command = "{} {} {} --dpi 300 --psm {} --oem 1 -c tessedit_do_invert=0 -l {}".format(tesseractPath, path, pngFilesPath, doc, lang)
			self.backgroundProcessing(command, totalPages, path)
			self.ocr.stop()
			self.creatTXTFromVariousTXT()

	def creatTXTFromVariousTXT(self):
		# If we are scanning, the final file with the results will be placed in "Documents" folder of user with the name ocr.txt.
		# If we are performing OCR to a image document, it will be placed in the same folder but with .txt extension.
		if scanning:
			# We are scanning, so get path of user documents folder
			documentsPath = self.get_documents_folder()
			outputFilePath = os.path.join(documentsPath, "OCR.txt")
		else:
			# We are recognizing an image file, so get its path
			baseName, _ = os.path.splitext(docPath)
			outputFilePath = (baseName + '.txt')[1:]
		# Join all recognized files in only one to simplify showing the results
		command = 'copy "%s" "%s"' %(os.path.join(PLUGIN_DIR, "images", "oc*.txt"), outputFilePath)
		subprocess.call(command, shell = True)
		self.showResults(outputFilePath)

	def convertPDFToTXT(self, docPath, outputFilePath):
		# Get the accessible text from the PDF file
		command = "{} -layout {} {}".format(pdf2TextPath, docPath, outputFilePath)
		totalPages = 0
		self.backgroundProcessing(command, totalPages, outputFilePath)

	def backgroundProcessing(self, command, totalPages, path):
		Command = command
		pages = totalPages
		file = path
		# Configs to avoid exibition of CMD
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		self.p = subprocess.Popen(Command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = self.p.communicate()
		# Treatment of some errors
		if "xpdf" in Command:
			if b"Syntax Warning: May not be a PDF file" in stderr:
				self.conv.stop()
				gui.messageBox(_("It is not a true PDF file!"), "TesseractOCR")
				return
				self.conv.stop()
				gui.messageBox(_("The PDF is password protected.\n\nIf you have introduced the password, make sure it is the correct one.\n\nOtherwise, please go to NVDA configurations, TesseractOCR options and mark the checkbox 'Ask for password'"), "TesseractOCR")
			if b"Command Line Error: Incorrect password" in stderr:
				self.conv.stop()
				return
			elif b"Unknown font in fields DA string" in stderr:
				pass
			elif stdout == b"":
				pass
		if pages == 0:
			self.showResults(file)

	def showResults(self, file):
		try:
			self.ocr.stop()
		except AttributeError:
			pass
		# Opening the TXT file with OCR results.
		z = ctypes.windll.shell32.ShellExecuteW(None, "open", file, None, None, 10)

	def doRoutines(self):
		self.conv = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		self.conv.start()
		# Convert PDF in PNG files compatibles with Tesseract...
		self.convertPDFToPNG()
		# Create the list of PNG files
		from .vars import listPath
		self.createList(".png")

	def doRoutines1(self):
		totalPages = 0
		# Perform OCR to the selected image file...
		self.OCR_image_files(docPath, totalPages)

	def doRoutines2(self):
		global scanning
		scanning = True
		self.scan = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		self.scan.start()
		# Digitalize page from scanner
		if not self._stop_event.is_set():  # Verify if the thread is signalized to stop
			ScanFromWia.run(self)
			if self._stop_event.is_set():
				# Process was stopped
				self.scan.stop()
				return
			# The process was not stopped, so lets keep running...
			self.scan.stop()
			self.createList(".jpg")
			scanning = False

	def doRoutines3(self, docPath):
		# Get the text from the PDF
		baseName, _ = os.path.splitext(docPath)
		outputFilePath = (baseName + '.txt')+"\""
		self.convertPDFToTXT(docPath, outputFilePath)

	@script(
		# Translators: Message to be announced during Keyboard Help
		description=_("Performs OCR to focused file in File Explorer"),
		category="TesseractOCR",
		gesture="kb:control+windows+r"
	)
	def script_OCRFile(self, gesture):
		from .vars import suppFiles
		# Check if we are in the Windows Explorer.
		fg = api.getForegroundObject()
		if fg.appModule.appName != "explorer":
			ui.message(_("You are not in File Explorer to perform OCR on an image file..."))
			return

		self.deleteFiles()

		global docPath
		docPath = self.getDocName()
		ext = docPath.split(".")[-1].lower()[:-1]
		if ext == "pdf":
			ui.message(_("Processing... Please wait... This operation can take some seconds..."))
			from .configPanel import shouldAskPwd
			shouldAskPwd = config.conf["tesseractOCR"]["askPassword"]
			if shouldAskPwd == True:
				self.dialog0 = Password(gui.mainFrame)
				if not self.dialog0.IsShown():
					gui.mainFrame.prePopup()
					self.dialog0.Show()
					gui.mainFrame.postPopup()
			# Starting the PDF recognition process
			self.recogPDF = threading.Thread(target = self.doRoutines)
			self.recogPDF.daemon = True
			self.recogPDF.start()

		elif ext in suppFiles:
			ui.message(_("Processing... Please wait... This operation can take some seconds..."))
			self.recogFile = threading.Thread(target=self.doRoutines1)
			self.recogFile.daemon = True
			self.recogFile.start()
		else:
			ui.message(_("File not supported"))

	@script(
		# For translators: Message to be announced during Keyboard Help
		description=_("Performs OCR to a document on the scanner"),
		category="TesseractOCR",
		gesture = "kb:control+windows+w"
	)
	def script_OCRFromScanner(self, gesture):
		# Delete the files from previous OCR
		self.deleteFiles()
		# Translators: Asking to wait untill the process is concluded
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		# Create the stop event for controlling the thread
		self._stop_event = threading.Event()
		# Starting the scanning and recognition process
		self.digitalize = threading.Thread(target = self.doRoutines2)
		self.digitalize.daemon = True
		self.digitalize.start()

	@script(
		# Translators: Message to be announced during Keyboard Help
		description=_("Gets the text from focused accessible PDF file in File Explorer"),
		category="TesseractOCR",
		gesture="kb:control+windows+t"
	)
	def script_GetText(self, gesture):
		# Check if we are in the Windows Explorer.
		fg = api.getForegroundObject()
		if fg.appModule.appName != "explorer":
			# Translators: Announcing we are not in File Explorer and the key stroke will not do anything...
			ui.message(_("You are not in File Explorer to perform OCR on a image file..."))
			return
		else:
			pass
		# Delete the files from previous OCR
		self.deleteFiles()
		# Obtain the full path of the selected file
		docPath = self.getDocName()
		# Check if is a supported file, and if yes if it is PDF or image file
		# The last [:-1] is to remove the last quote sign...
		ext = docPath.split(".")[-1].lower()[:-1]
		if ext == "pdf":
			# Translators: Asking to wait untill the process is concluded
			ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
			# Starting the process
			self.doRoutines3(docPath)
		else:
			# Translators: Informing that the file is not from supported types...
			ui.message(_("File not supported"))

	@script(
		# Translators: Message to be announced during Keyboard Help
		description=_("Cancel scanning"),
		category="TesseractOCR",
		gesture="kb:control+windows+c"
	)
	def script_stopScanning(self, gesture):
		from .scanFromWia import scan_thread  # Import the global scan_thread from scanFromWia
		global scan_thread
		# Stop the scanning thread if it exists
		if scan_thread and scan_thread.is_alive():
			scan_thread.stop()
			if hasattr(self, 'digitalize') and self.digitalize.is_alive():
				self._stop_event.set()  # Signal to stop the digitalize thread
		try:
			self.p.kill()
		except AttributeError:
			pass
		if hasattr(self, 'scan') and self.scan.is_alive():
			self.scan.stop()
		if hasattr(self, 'recogPDF') and self.recogPDF.is_alive():
			self.recogPDF.stop()
		if hasattr(self, 'recogFile') and self.recogFile.is_alive():
			self.recogFile.stop()
		# Translators: Informing user the process was terminated
		ui.message(_("Scanning process terminated!"))


class Password(wx.Dialog):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetTitle("TesseractOCR")

		sizer_1 = wx.BoxSizer(wx.VERTICAL)

		# Translators: Asking user to enter the PDF password
		label_1 = wx.StaticText(self, wx.ID_ANY, _("Enter your password"))
		sizer_1.Add(label_1, 0, 0, 0)

		self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
		self.text_ctrl_1.SetFocus()
		sizer_1.Add(self.text_ctrl_1, 0, 0, 0)

		sizer_2 = wx.StdDialogButtonSizer()
		sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

		self.button_OK = wx.Button(self, wx.ID_OK, "")
		self.button_OK.SetDefault()
		sizer_2.AddButton(self.button_OK)

		self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
		sizer_2.AddButton(self.button_CANCEL)

		sizer_2.Realize()

		self.SetSizer(sizer_1)
		sizer_1.Fit(self)

		self.SetAffirmativeId(self.button_OK.GetId())
		self.SetEscapeId(self.button_CANCEL.GetId())

		self.Layout()
		self.CentreOnScreen()

		self.Bind(wx.EVT_TEXT_ENTER, self.onOkButton, self.text_ctrl_1)
		self.Bind(wx.EVT_BUTTON, self.onOkButton, self.button_OK)

	def onOkButton(self, event):
		global pwd
		pwd = self.text_ctrl_1.GetValue()
		self.Destroy()
		return pwd
		event.Skip()

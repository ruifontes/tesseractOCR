#-*- coding: utf-8 -*-
# Main file for Tesseract OCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2020-2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
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

from comtypes.client import CreateObject as COMCreate
import shutil
import ui
import gui
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel
from gui import guiHelper
import time
from scriptHandler import script
import languageHandler
from .runInThread import *
from .vars import *
# For translation process
addonHandler.initTranslation()

# Place tessdata in PYTHONPATH
sys.path.append(os.path.join(PLUGIN_DIR, "tesseract", "tessdata"))
del sys.path[-1]
os.environ['OMP_THREAD_LIMIT'] = '1'

docPath = ""
showPwdValue = False
pwd = ""
jpgFilePath = ""
endTask = False

initConfiguration()

if globalVars.appArgs.secure:
	# Override the global plugin to disable it.
	GlobalPlugin = globalPluginHandler.GlobalPlugin


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		# Call of the constructor of the parent class.
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		# Adding a NVDA configurations section
		from .configPanel import OCRSettingsPanel
		gui.NVDASettingsDialog.categoryClasses.append(OCRSettingsPanel)
		self._thread = None

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		from .configPanel import OCRSettingsPanel
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(OCRSettingsPanel)

	def deleteFiles(self):
		from .vars import listPath
		# Delete the temporary images folder and create again
		shutil.rmtree(os.path.join(PLUGIN_DIR, "images"), ignore_errors=True)
		os.mkdir(os.path.join(PLUGIN_DIR, "images"))
		# Delete the temporary list file
		try:
			filePath = listPath[1:-1]
			os.remove(filePath)
		except FileNotFoundError:
			pass

	def getDocName(self):
		docPath = ""
		# getting file path and name
		fg = api.getForegroundObject()
		# We check if we are in the Windows Explorer.
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
		else: # loop exhausted
			desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
			docPath = '\"' + desktop_path + '\\' + api.getDesktopObject().objectWithFocus().name + '\"'
			return
		# Now that we have the current folder, we can explore the SelectedItems collection.
		targetFile= focusedItem.path
		docPath = '\"'+str(targetFile)+'\"'
		return docPath

	def convertPDFToPNG():
		from .vars import pdf2PNGPath, pngFilesPath
		from .configPanel import shouldAskPwd
		# Transform PDF files in PNG files, since PDF format is not accepted by Tesseract...
		# Check if should ask for password
		shouldAskPwd = config.conf["tesseractOCR"]["askPassword"]
		if shouldAskPwd == True and pwd != "":
			command = "{} -r 300 -gray -upw {} {} {}".format(pdf2PNGPath, pwd, docPath, pngFilesPath)
		else:
			command = "{} -r 300 -gray {} {}".format(pdf2PNGPath, docPath, pngFilesPath)
		GlobalPlugin.backgroundProcessing(command)

	def createPNGList():
		from .vars import listPath
		# Check the PNG files created and list them in list.txt...
		items = os.listdir(os.path.join(PLUGIN_DIR, "images"))
		list = []
		for names in items:
			if names.endswith(".png"):
				list.append(os.path.join(PLUGIN_DIR, "images", names))
		if len(list) != 0:
			with open(listPath[1:-1], "w", encoding = "latin1") as f:
				for x in range(len(list)):
					f.write(list[x]+"\n")
				f.close()
			# Perform OCR to all PNG files in the list.txt
			GlobalPlugin.OCR_image_files(listPath)
		else:
			return

	def digitalizeDocument(self):
		from .vars import wiaCMDPath, wiaCwd
		global endTask, num, jpgFilePath
		# Create routine for multiple scannings
		num = ""
		n = 1
		while n <= 999:
			num = "{:03d}".format(n)
			jpgFilePath = os.path.join(PLUGIN_DIR, "images", "ocr"+num+".jpg")
			# Digitalize one page from scanner
			command = "{} /w 0 /h 0 /dpi {} /color {} /format JPG /output {} cwd = {}".format(
				wiaCMDPath,
				300,
				"GRAY",
				jpgFilePath,
				wiaCwd
			)
			GlobalPlugin.backgroundProcessing(command)
			# Check if are more pages to scan...
			if gui.messageBox(_("Do you want to scan one more page?"), "TesseractOCR", style=wx.ICON_QUESTION|wx.YES_NO) == wx.YES:
				# More pages to scan...
				n+= 1
				# Wait until file be put on right local
				while not  os.path.exists(jpgFilePath):
					time.sleep(0.01)
				self.scan.stop()
			else:
				# No more pages to scan...
				# Wait until file be put on right local
				while not  os.path.exists(jpgFilePath):
					time.sleep(0.01)
				self.scan.stop()
				endTask = True
				break
		# Job done, so prepare image files to be recognized
		GlobalPlugin.createJPGList()

	def createJPGList():
		from .vars import listPath
		# Check the jPG files created and list them in list.txt...
		items = os.listdir(os.path.join(PLUGIN_DIR, "images"))
		list = []
		for names in items:
			if names.endswith(".jpg"):
				list.append(os.path.join(PLUGIN_DIR, "images", names))
		if len(list) != 0:
			with open(listPath[1:-1], "w", encoding = "latin1") as f:
				for x in range(len(list)):
					f.write(list[x]+"\n")
				f.close()
			# Perform OCR to all JPG files in the list.txt
			GlobalPlugin.OCR_image_files(listPath)
		else:
			return

	def OCR_image_files(path):
		global endTask
		from .vars import tesseractPath, pngFilesPath
		from .configPanel import lang, doc
		if doc == 1:
			lang = "osd"+"+"+lang
		GlobalPlugin.ocr = runInThread.RepeatBeep(delay=2.0, beep=(300, 300), isRunning=None)
		GlobalPlugin.ocr.start()
		Path = path
		# Perform OCR to the selected image file
		command = "{} {} {} --dpi 300 --psm {} --oem 1 -c tessedit_do_invert=0 -l {} quiet pdf".format(tesseractPath, Path, pngFilesPath, doc, lang)
		GlobalPlugin.backgroundProcessing(command)
		GlobalPlugin.showResults()
		endTask = False

	def backgroundProcessing(command):
		Command = command
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		p = subprocess.Popen(Command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()
		if "wia" in Command:
			if b"finished" not in (stderr or stdout) and (stderr or stdout) != b"":
				message = _("Process wia-cmd-scanner failed:\n") + "{error}".format(error=stderr.decode() if stderr else stdout.decode()+_("\nPlease make sure your scanner is WIA-compliant and can scan in another application before trying again!"))
				gui.messageBox (_("Scan error\n")+message, "TesseractOCR")
		elif "xpdf" in Command:
			if b"Syntax Warning: May not be a PDF file" in stderr:
				GlobalPlugin.conv.stop()
				gui.messageBox(_("It is not a true PDF file!"), "TesseractOCR")
				return
			if b"Command Line Error: Incorrect password" in stderr:
				GlobalPlugin.conv.stop()
				gui.messageBox(_("The PDF is password protected.\n\nIf you have introduced the password, make sure it is the correct one.\n\nOtherwise, please go to NVDA configurations, TesseractOCR options and mark the checkbox 'Ask for password'"), "TesseractOCR")
				return
			elif b"Unknown font in field's DA string" in stderr:
				pass
			elif stdout == b"":
				pass
			GlobalPlugin.conv.stop()

	def showResults():
		GlobalPlugin.ocr.stop()
		# Opening the PDF file with OCR results.
		z = ctypes.windll.shell32.ShellExecuteW(None, "open", os.path.join(PLUGIN_DIR, "images", "ocr.pdf"), None, None, 10)

	def doRoutines(self):
		GlobalPlugin.conv = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		GlobalPlugin.conv.start()
		# Convert PDF in PNG files compatibles with Tesseract...
		GlobalPlugin.convertPDFToPNG()
		# Create the list of PNG files
		from .vars import listPath
		GlobalPlugin.createPNGList()

	def doRoutines1(self):
		# Perform OCR to the selected image file...
		GlobalPlugin.OCR_image_files(docPath)

	def doRoutines2(self):
		self.scan = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		self.scan.start()
		# Digitalize page from scanner
		self.digitalizeDocument()

	@script( 
		# For translators: Message to be announced during Keyboard Help 
		description = _("Performs OCR to focused file in File Explorer"), 
		category = "TesseractOCR", 
		gesture = "kb:control+windows+r")
	def script_OCRFile(self, gesture):
		from .vars import suppFiles
		# Delete the files from previous OCR
		self.deleteFiles()
		# Translators: Asking to wait untill the process is concluded
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		# Obtain the full path of the selected file
		global docPath
		docPath = self.getDocName()
		# Check if is a supported file, and if yes if it is PDF or image file
		ext = docPath.split(".")[-1].lower()[:-1]  # The last [:-1] is to remove the last " sign...
		if ext == "pdf":
			from .configPanel import shouldAskPwd
			if shouldAskPwd == True:
				gui.mainFrame._popupSettingsDialog(Password)
			else:
				# Starting the PDF recognition process
				self.recogPDF = threading.Thread(target = self.doRoutines)
				self.recogPDF.setDaemon(True)
				self.recogPDF.start()
		elif (ext in suppFiles):
			# Starting the image file recognition process
			self.recogFile = threading.Thread(target = self.doRoutines1)
			self.recogFile.setDaemon(True)
			self.recogFile.start()
		else:
			# Translators: Informing that the file is not from supported types...
			ui.message(_("File not supported"))

	@script(
		# For translators: Message to be announced during Keyboard Help 
		description = _("Performs OCR to a document on the scanner"), 
		category = "TesseractOCR", 
		gesture = "kb:control+windows+w")
	def script_OCRFromScanner(self, gesture):
		# Delete the files from previous OCR
		self.deleteFiles()
		# Translators: Asking to wait untill the process is concluded
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		# Starting the scanning and recognition process
		self.digitalize = threading.Thread(target = self.doRoutines2)
		self.digitalize.setDaemon(True)
		self.digitalize.start()


class Password(wx.Dialog):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetTitle(_("TesseractOCR"))

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
		# Starting the PDF recognition process
		self.recogPDF = threading.Thread(target = GlobalPlugin.doRoutines(GlobalPlugin))
		self.recogPDF.setDaemon(True)
		self.recogPDF.start()
		event.Skip()
		# To reset the password...
		pwd = ""


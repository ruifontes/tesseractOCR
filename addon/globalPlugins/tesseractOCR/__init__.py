#-*- coding: utf-8 -*-
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2020-2022 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

import globalPluginHandler
import ui
import sys
import os
import threading
import subprocess
import api
import ctypes
import controlTypes
if hasattr(controlTypes, "Role"):
	for r in controlTypes.Role: setattr(controlTypes, r.__str__().replace("Role.", "ROLE_"), r)
else:
	setattr(controlTypes, "Role", type('Enum', (), dict([(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))

if hasattr(controlTypes, "State"):
	for r in controlTypes.State: setattr(controlTypes, r.__str__().replace("State.", "STATE_"), r)
else:
	setattr(controlTypes, "State", type('Enum', (), dict([(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))

from comtypes.client import CreateObject as COMCreate
import time
from . import runInThread
from scriptHandler import script
import languageHandler
# For update process
from .update import *
# For translation
import addonHandler
addonHandler.initTranslation()

from .vars import PLUGIN_DIR
# Place tessdata in PYTHONPATH
sys.path.append(os.path.join(PLUGIN_DIR, "tesseract", "tessdata"))
del sys.path[-1]

docPath = ""

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

		# To allow waiting end of network tasks
		core.postNvdaStartup.register(self.networkTasks)

	def networkTasks(self):
		# Calling the update process...
		_MainWindows = Initialize()
		_MainWindows.start()

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		core.postNvdaStartup.unregister(self.networkTasks)
		from .configPanel import OCRSettingsPanel
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(OCRSettingsPanel)

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

	def backgroundProcessing(self, command):
		self.command = command
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		p = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()
		#if b"finished" not in (stderr or stdout) and (stderr or stdout) != b"":
			#raise RuntimeError("Subprocess wia-cmd-scanner failed:\n {error}".format(error=stderr.decode()) if stderr else stdout.decode())
			#self.digitalize.stop()

	def convertPDFToPNG(self):
		from .vars import pdf2PNGPath, pngFilesPath
		# Transform PDF files in PNG files, since those are accepted by Tesseract...
		command = "{} -r 400 -gray {} {}".format(pdf2PNGPath, docPath, pngFilesPath)
		self.backgroundProcessing(command)

	def createList(self):
		from .vars import listPath
		# Check the PNG files created and list them in list.txt...
		items = os.listdir(os.path.join(PLUGIN_DIR, "images"))
		list = []
		for names in items:
			if names.endswith(".png"):
				list.append(os.path.join(PLUGIN_DIR, "images", names))
		with open(listPath[1:-1], "w", encoding = "latin1") as f:
			for x in range(len(list)):
				f.write(list[x]+"\n")
			f.close()

	def digitalizeDocument(self):
		from .vars import wiaCMDPath, jpgFilePath, wiaCwd
		# Digitalize one page from scanner
		command = "{} /w 0 /h 0 /dpi {} /color {} /format JPG /output {} cwd = {}".format(
		wiaCMDPath,
		300,
		"GRAY",
		jpgFilePath,
		wiaCwd
		)
		self.backgroundProcessing(command)

	def OCR_image_files(self, path):
		from .vars import tesseractPath, pngFilesPath
		from .configPanel import lang, doc
		if doc == 1:
			lang = "osd"+"+"+lang
		self.ocr = runInThread.RepeatBeep(delay=2.0, beep=(300, 300), isRunning=None)
		self.ocr.start()
		self.path = path
		# Perform OCR to the selected image file
		command = "{} {} {} --dpi 300 --psm {} --oem 1 -l {} quiet".format(tesseractPath, self.path, pngFilesPath, doc, lang)
		self.backgroundProcessing(command)
		self.ocr.stop()
		self.showResults()

	def showResults(self):
		from .vars import ocrTxtPath
		# Opening the TXT file with OCR results.
		z = ctypes.windll.shell32.ShellExecuteW(None, "open", ocrTxtPath, None, None, 10)

	def deleteFiles(self):
		from .vars import listPath
		# Delete the temporary images folder
		shutil.rmtree(os.path.join(PLUGIN_DIR, "images"), ignore_errors=True)
		os.mkdir(os.path.join(PLUGIN_DIR, "images"))
		# Delete the temporary list file
		try:
			filePath = listPath[1:-1]
			os.remove(filePath)
		except FileNotFoundError:
			pass

	def _doRoutines(self):
		from .vars import listPath
		self.conv = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		self.conv.start()
		# Convert PDF in PNG files compatibles with Tesseract...
		self.convertPDFToPNG()
		# Create the list of PNG files
		self.createList()
		self.conv.stop()
		# Perform OCR to all PNG files in the list.txt
		self.OCR_image_files(listPath)

	def _doRoutines1(self):
		# Perform OCR to the selected image file...
		self.OCR_image_files(docPath)

	def _doRoutines2(self):
		from .vars import jpgFilePath
		self.scan = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		self.scan.start()
		# Digitalize page from scanner
		self.digitalizeDocument()
		# Perform OCR to the JPG created...
		# Wait until file be put on right local
		while not  os.path.exists(jpgFilePath):
			time.sleep(0.01)
		if os.path.exists(jpgFilePath):
			self.scan.stop()
			# We already have the file, so recognize it...
			self.OCR_image_files(jpgFilePath)

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
		ext = docPath[-5:-1].lower()
		if ext == ".pdf":
			# Starting the PDF recognition process
			self.recogPDF = threading.Thread(target = self._doRoutines)
			self.recogPDF.setDaemon(True)
			self.recogPDF.start()
		elif (str(ext) in suppFiles):
			# Starting the image file recognition process
			self.recogFile = threading.Thread(target = self._doRoutines1)
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
		self.digitalize = threading.Thread(target = self._doRoutines2)
		self.digitalize.setDaemon(True)
		self.digitalize.start()

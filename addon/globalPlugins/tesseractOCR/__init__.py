#-*- coding: utf-8 -*-
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2020-2022 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

import globalPluginHandler
import gui
import wx
import ui
import sys
import os
import threading
import subprocess
from subprocess import Popen, PIPE
import ctypes
import tones
import config
import api
from comtypes.client import CreateObject as COMCreate
import time
from scriptHandler import script
import languageHandler
# For update process
from .update import *
import addonHandler
addonHandler.initTranslation()

docPath = ""
suppFiles = [".bmp", ".pnm", ".pbm", ".pgm", ".png", ".jpg", ".jp2", ".gif", ".tif", "jfif", "jpeg", "tiff", "spix", "webp"]
lang = ""
doc = ""
PLUGIN_DIR = os.path.dirname(__file__)

# Place tessdata in PYTHONPATH
sys.path.append(os.path.join(PLUGIN_DIR, "tesseract", "tessdata"))
del sys.path[-1]

tesseractPath = "\""+os.path.join (PLUGIN_DIR, "tesseract", "tesseract.exe")+"\""
pngFilesPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr")+"\""
listPath = os.path.join (PLUGIN_DIR, "list.txt")
ocrTxtPath = os.path.join (PLUGIN_DIR, "images", "ocr.txt")

#Based on the OCR add-on from NVAccess:
localesToTesseractLangs = {
"af" : "afr",
"am" : "amh",
"ar" : "ara",
"bg" : "bul",
"ca" : "cat",
"cs" : "ces",
"zh_CN" : "chi_sim",
"zh_HK" : "chi_tra",
"da" : "dan",
"de" : "deu",
"el" : "ell",
"en" : "eng",
"fa" : "fas",
"fi" : "fin",
"fr" : "fra",
"ga" : "gle",
"gl" : "glg",
"he" : "heb",
"hi" : "hin",
"hr" : "hrv",
"hu" : "hun",
"id" : "ind",
"is" : "isl",
"it" : "ita",
"ja" : "jpn",
"kn" : "kan",
"ka" : "kat",
"ky" : "kir",
"ko" : "kor",
"lv" : "lav",
"lt" : "lit",
"mk" : "mkd",
"my" : "mya",
"ne" : "nep",
"nl" : "nld",
"nb_NO" : "nor",
"pa" : "pan",
"pl" : "pol",
"pt" : "por",
"ro" : "ron",
"ru" : "rus",
"sk" : "slk",
"sl" : "slv",
"es" : "spa",
"sr" : "srp_latn",
"sv" : "swe",
"ta" : "tam",
"th" : "tha",
 "tr" : "tur",
"uk" : "ukr",
"ur" : "urd",
"vi" : "vie"
}
tesseractLangsToLocales = {v : k for k, v in localesToTesseractLangs.items()}

def getAvailableTesseractLanguages():
	dataDir = os.path.join(os.path.dirname(__file__), "tesseract", "tessdata")
	dataFiles = [file for file in os.listdir(dataDir) if file.endswith('.traineddata')]
	return [os.path.splitext(file)[0] for file in dataFiles]

def getDefaultLanguage():
	global lang
	lang = languageHandler.getLanguage()
	if lang not in localesToTesseractLangs and "_" in lang:
		lang = lang.split("_")[0]
	return localesToTesseractLangs.get(lang, "eng")

lng = getDefaultLanguage()

config.conf["tesseractOCR"] = {}
config.conf["tesseractOCR"]["language"] = lng
config.conf["tesseractOCR"]["docType"] = 6


class OCRSettingsPanel(gui.SettingsPanel):
	# Translators: Title of the OCR settings dialog in the NVDA settings.
	title = "TesseractOCR"

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer = settingsSizer)
		# Translators: Label of a  combobox used to choose a recognition language
		recogLanguageLabel = _("Recognition &language")
		self.availableLangs = {languageHandler.getLanguageDescription(tesseractLangsToLocales[lang]) or tesseractLangsToLocales[lang] : lang for lang in getAvailableTesseractLanguages()}
		self.recogLanguageCB = sHelper.addLabeledControl(
			recogLanguageLabel,
			wx.Choice,
			choices = list(self.availableLangs.keys()),
			style = wx.CB_SORT
		)
		tessLangsToDescs = {v : k  for k, v in self.availableLangs.items()}
		curlang = config.conf["tesseractOCR"]["language"]
		try:
			select = tessLangsToDescs[curlang]
		except ValueError:
			select = tessLangsToDescs['eng']
		select = self.recogLanguageCB.FindString(select)
		self.recogLanguageCB.SetSelection(select)

		# Translators: Label of a  combobox used to choose a type of document to recognize
		recogDocTypeLabel = _("&Type of document")
		DOC_ALL = 3
		DOC_TEXT = 6
		DOC_LABELS = {
			# Translators: The entry for various types of docs, invoices, bills, magazines and so on....
			DOC_ALL : pgettext("docType", _("Various")),
			# Translators: The entry for text only, like books and letters for instance...
			DOC_TEXT : pgettext("docType", _("Text"))
		}
		self.docTypesLabel = (DOC_ALL, DOC_TEXT)
		self.docTypesChoices = [DOC_LABELS[Type] for Type in self.docTypesLabel]
		self.recogDocTypeCB = sHelper.addLabeledControl(
			recogDocTypeLabel,
			wx.Choice,
			choices = list(self.docTypesChoices),
			style = wx.CB_SORT
		)
		curLevel  = int(config.conf["tesseractOCR"]["docType"])
		self.recogDocTypeCB.SetSelection(self.docTypesLabel.index(curLevel))

		# Translators: Checkbox name in the configuration dialog
		self.shouldUpdateChk = sHelper.addItem(wx.CheckBox(self, label=_("Check for updates at startup")))
		self.shouldUpdateChk.SetValue(config.conf[ourAddon.name]["isUpgrade"])
		if config.conf.profiles[-1].name:
			self.shouldUpdateChk.Disable()

	def onSave (self):
		lang = self.availableLangs[self.recogLanguageCB.GetStringSelection()]
		config.conf["tesseractOCR"]["language"] = lang
		doc = self.docTypesChoices[self.recogDocTypeCB.GetSelection()]
		if doc == pgettext("docType", _("Text")):
			doc = 6
		else:
			doc = 3
		config.conf["tesseractOCR"]["docType"] = doc
		if not config.conf.profiles[-1].name:
			config.conf[ourAddon.name]["isUpgrade"] = self.shouldUpdateChk.GetValue()

# End of code based on the same class of OCR add-on from NVAccess:

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

		# To allow waiting end of network tasks
		core.postNvdaStartup.register(self.networkTasks)

	def networkTasks(self):
		# Calling the update process...
		_MainWindows = Initialize()
		_MainWindows.start()

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		core.postNvdaStartup.unregister(self.networkTasks)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(ClipSpeakSettingsPanel)

	def getDocName(self):
		# getting file path and name
		global docPath
		path = ""
		fg = api.getForegroundObject()
		# We check if we are in the Windows Explorer.
		if fg.role != api.controlTypes.Role.PANE and fg.appModule.appName != "explorer":
			return
		# self.shell = self.shell or ct.client.CreateObject("shell.application")
		self.shell = COMCreate("shell.application")
		# We go through the list of open Windows Explorers to find the one that has the focus.
		for window in self.shell.Windows():
			if window.hwnd == fg.windowHandle:
				focusedItem=window.Document.FocusedItem
				break
		else: # loop exhausted
			desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
			docPath = desktop_path + '\\' + api.getDesktopObject().objectWithFocus().name
			return
		# Now that we have the current folder, we can explore the SelectedItems collection.
		targetFile= focusedItem.path
		docPath = '\"'+str(targetFile)+'\"'

	def convertPDFToPNG(self):
		# Transform PDF files in PNG files, since those are accepted by Tesseract...
		# Address of the tool to do that...
		pdf2PNGPath = "\""+os.path.join (PLUGIN_DIR, "xpdf-tools", "pdftopng.exe")+"\""
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		command = "{} -r 400 -gray {} {}".format(pdf2PNGPath, docPath, pngFilesPath)
		p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()

	def createList(self):
		# Check the PNG files created and list them in list.txt...
		items = os.listdir(os.path.join(PLUGIN_DIR, "images"))
		list = []
		for names in items:
			if names.endswith(".png"):
				list.append(os.path.join(PLUGIN_DIR, "images", names))
		with open(listPath, "w", encoding = "latin1") as f:
			for x in range(len(list)):
				f.write(list[x]+"\n")
			f.close()

	def OCR_PNG_files(self):
		# Perform OCR in all PNG files created using list.txt created above...
		global lang, doc
		lang = config.conf["tesseractOCR"]["language"]
		doc = str(config.conf["tesseractOCR"]["docType"])
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		command = "{} {} {} --dpi 400 --psm {} -l {} quiet".format(tesseractPath, listPath, pngFilesPath, doc, lang)
		p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()
		self.showResults()

	def OCR_image_files(self):
		# Perform OCR to the selected image file
		global lang, doc
		lang = config.conf["tesseractOCR"]["language"]
		doc = str(config.conf["tesseractOCR"]["docType"])
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		command = "{} {} {} --dpi 400 --psm {} -l {} quiet".format(tesseractPath, docPath, pngFilesPath, doc, lang)
		p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()
		self.showResults()

	def digitalizeDocument(self):
		# Digitalize one page from scanner
		jpgBatPath = os.path.join(PLUGIN_DIR, "ocr.bat")
		wiaCMDPath = os.path.join (PLUGIN_DIR, "wia-cmd-scanner")
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		command = "{} cwd={}".format(jpgBatPath, wiaCMDPath)
		p = Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()

	def showResults(self):
		# Opening the TXT file with OCR results.
		z = ctypes.windll.shell32.ShellExecuteW(None, "open", ocrTxtPath, None, None, 10)

	def deleteFiles(self):
		# Delete the temporary files...
		os.system("del "+str(os.path.join(PLUGIN_DIR, "images", "*.*"))+" /q")

	def _doRoutines(self):
		# Convert PDF in PNG files compatibles with Tesseract...
		self.convertPDFToPNG()
		# Create the list of PNG files
		self.createList()
		# Perform OCR to all PNG files in the list.txt
		self.OCR_PNG_files()

	def _doRoutines1(self):
		# Perform OCR to the selected image file...
		self.OCR_image_files()

	def _doRoutines2(self):
		# Digitalize page from scanner
		self.digitalizeDocument()
		# Perform OCR to the JPG created...
		jpgFilePath = os.path.join(PLUGIN_DIR, "images", "ocr.jpg")
		global lang, doc
		lang = config.conf["tesseractOCR"]["language"]
		doc = str(config.conf["tesseractOCR"]["docType"])
		# Wait until file be put on right local
		while not  os.path.exists(jpgFilePath):
			time.sleep(0.01)
		if os.path.exists(jpgFilePath):
			si = subprocess.STARTUPINFO()
			si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			command = "{} {} {} --dpi 400 --psm {} -l {} quiet".format(tesseractPath, jpgFilePath, pngFilesPath, doc, lang)
			p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
			stdout, stderr = p.communicate()
		self.showResults()

	@script( 
		# For translators: Message to be announced during Keyboard Help 
		description = _("Performs OCR to focused file in File Explorer"), 
		category = "TesseractOCR", 
		gesture = "kb:control+windows+r")
	def script_OCRFile(self, gesture):
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		# Delete the files from preview OCR
		self.deleteFiles()
		# Obtain the full path of the selected file
		self.getDocName()
		# Check if is a supported file, and if yes if it is PDF or image file
		ext = os.path.splitext(docPath)[-1].lower().replace(r'"', '')
		if ext == ".pdf":
			self._thread = threading.Thread(target = self._doRoutines)
			self._thread.setDaemon(True)
			self._thread.start()
		elif (str(ext) in suppFiles):
			self._thread = threading.Thread(target = self._doRoutines1)
			self._thread.setDaemon(True)
			self._thread.start()
		else:
			ui.message(_("File not supported"))

	@script( 
		# For translators: Message to be announced during Keyboard Help 
		description = _("Performs OCR to a document on the scanner"), 
		category = "TesseractOCR", 
		gesture = "kb:control+windows+Shift+r")
	def script_OCRFromScanner(self, gesture):
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		# Delete the files from preview OCR
		self.deleteFiles()
		self._thread = threading.Thread(target = self._doRoutines2)
		self._thread.setDaemon(True)
		self._thread.start()

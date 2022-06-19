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
from scriptHandler import script
import languageHandler
# For update process
from .update import *
# For translation
import addonHandler
addonHandler.initTranslation()

docPath = ""
suppFiles = [".bmp", ".pnm", ".pbm", ".pgm", ".png", ".jpg", ".jp2", ".gif", ".tif", "jfif", "jpeg", "tiff", "spix", "webp"]
lang = ""
doc = ""
lng = ""
PLUGIN_DIR = os.path.dirname(__file__)
tesseractPath = "\""+os.path.join (PLUGIN_DIR, "tesseract", "tesseract.exe")+"\""
pngFilesPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr")+"\""
listPath = "\""+os.path.join (PLUGIN_DIR, "list.txt")+"\""
ocrTxtPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr.txt")+"\""

# Place tessdata in PYTHONPATH
sys.path.append(os.path.join(PLUGIN_DIR, "tesseract", "tessdata"))
del sys.path[-1]

initConfiguration()

tesseractLangs = [
	"afr",
	"amh",
	"ara",
	"bul",
	"cat",
	"ces",
	"chi_sim",
	"chi_tra",
	"dan",
	"deu",
	"ell",
	"eng",
	"fas",
	"fin",
	"fra",
	"gle",
	"glg",
	"heb",
	"hin",
	"hrv",
	"hun",
	"ind",
	"isl",
	"ita",
	"jpn",
	"kan",
	"kat",
	"kir",
	"kor",
	"lav",
	"lit",
	"mkd",
	"mya",
	"nep",
	"nld",
	"nor",
	"pan",
	"pol",
	"por",
	"ron",
	"rus",
	"slk",
	"slv",
	"spa",
	"srp_latn",
	"swe",
	"tam",
	"tha",
	"tur",
	"ukr",
	"urd",
	"vie"
]

#Based on the OCR add-on from NVAccess:
# Correspondence between language code of NVDA and Tesseract
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

# Correspondence between language codes between Tesseract and NVDA
tesseractLangsToLocales = {v : k for k, v in localesToTesseractLangs.items()}

def getAvailableTesseractLanguages():
	# Path of folder containing the .traineddata files responsible for OCR language...
	dataDir = os.path.join(os.path.dirname(__file__), "tesseract", "tessdata")
	# List of files...
	dataFiles = [file for file in os.listdir(dataDir) if file.endswith('.traineddata')]
	# Create a list only with the lang name...
	return [os.path.splitext(file)[0] for file in dataFiles]

def getDefaultLanguage():
	global lang
	lang = languageHandler.getLanguage()
	if lang not in localesToTesseractLangs and "_" in lang:
		lang = lang.split("_")[0]
	return localesToTesseractLangs.get(lang, "eng")

lng = getDefaultLanguage()


class OCRSettingsPanel(gui.SettingsPanel):
	# Translators: Title of the OCR settings dialog in the NVDA settings.
	title = "TesseractOCR"

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer = settingsSizer)
		# Translators: Label of a  combobox used to choose a recognition language
		recogLanguageLabel = _("Recognition &language")
		# Get the dict of available langs
		self.availableLangs = {languageHandler.getLanguageDescription(tesseractLangsToLocales[lang]) or tesseractLangsToLocales[lang] : lang for lang in getAvailableTesseractLanguages()}
		self.recogLanguageCB = sHelper.addLabeledControl(
			recogLanguageLabel,
			wx.Choice,
			choices = list(self.availableLangs.keys()),
			style = wx.CB_SORT
		)
		tessLangsToDescs = {v : k  for k, v in self.availableLangs.items()}
		try:
			if config.conf["tesseractOCR"]["language"]:
				# Record exist, so use it...
				curlang = config.conf["tesseractOCR"]["language"]
		except:
			# Record do not exist, so use NVDA language
			curlang = lng
		try:
			# Get lang description
			select = tessLangsToDescs[curlang]
		except ValueError:
			# Do not exist, so use english...
			select = tessLangsToDescs['eng']
		# Get the index of the language
		select = self.recogLanguageCB.FindString(select)
		# Set selection to the index of lang
		self.recogLanguageCB.SetSelection(select)

		# Translators: Label of a  combobox used to choose a type of document to recognize
		recogDocTypeLabel = _("&Type of document")
		DOC_ALL = 3
		DOC_TEXT = 6
		DOC_LABELS = {
			# Translators: The entry for various types of docs, invoices, bills, magazines and so on...
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

		global missingTrainedData, availableTrainedDataList, tesseractLangsList
		# Get the available trainedData from the folder
		availableTrainedDataList = getAvailableTesseractLanguages()
		tesseractLangsList = tesseractLangs
		missingTrainedData = []
		n = 0
		while n < len(tesseractLangsList):
			if tesseractLangsList[n] not in availableTrainedDataList:
				# False, so join to missing trainedData list...
				missingTrainedData.append(tesseractLangsList[n])
				# And delete from available trainedData list
				del tesseractLangsList[n]
				# To allow to check all list since we have deleted the item with number n...
				n -= 1
			n += 1

		# Translators: Label of a  combobox used to choose a recognition language to import the data files
		importLanguageLabel = _("&Import language")
		self.availableTrainedDataDict = {languageHandler.getLanguageDescription(tesseractLangsToLocales[lang]) or tesseractLangsToLocales[lang] : lang for lang in missingTrainedData}
		self.importLanguageCB = sHelper.addLabeledControl(importLanguageLabel, wx.Choice, choices = list(self.availableTrainedDataDict.keys()), style = wx.CB_SORT)

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

		# Routine to download the files to the right folder...
		# Get the language name of file to download
		ocrLang = self.availableTrainedDataDict[self.importLanguageCB.GetStringSelection()]
		# Construct the name of file to download
		urlN = ocrLang + ".traineddata"
		# Online repository of files
		urlRepos = "https://www.tiflotecnia.net/traineddata/"
		# Full URL of the dictionary file...
		urlName = urlRepos + urlN
		# Full path where to save the dictionary
		filepath = os.path.join (os.path.dirname(__file__), "tesseract", "tessdata")
		file = os.path.join(filepath, urlN)
		# Download the file content
		req = urllib.request.Request(urlName, headers={'User-Agent': 'Mozilla/5.0'})
		response = urllib.request.urlopen(req)
		fileContents = response.read()
		response.close()

		# Save the content in our file
		f = open(file, "wb")
		f.write(fileContents)
		f.close()

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
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(OCRSettingsPanel)

	def getDocName(self):
		# getting file path and name
		global docPath
		docPath = ""
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
		with open(listPath[1:-1], "w", encoding = "latin1") as f:
			for x in range(len(list)):
				f.write(list[x]+"\n")
			f.close()

	def OCR_image_files(self, path):
		self.path = path
		# Perform OCR to the selected image file
		global lang, doc
		try:
			lang = config.conf["tesseractOCR"]["language"]
		except KeyError:
			lang = lng
		doc = str(config.conf["tesseractOCR"]["docType"])
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		command = "{} {} {} --dpi 300 --psm {} -l {} quiet".format(tesseractPath, self.path, pngFilesPath, doc, lang)
		p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()
		self.showResults()

	def digitalizeDocument(self):
		# Digitalize one page from scanner
		# The next two lines are to prevent the cmd from being displayed.
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		command = "{exe} /w 0 /h 0 /dpi {dpi} /color {color} /format JPG /output {output} cwd={cwd}".format(
		exe = os.path.join(PLUGIN_DIR, "wia-cmd-scanner", "wia-cmd-scanner.exe"),
		dpi = 300,
		color = "GRAY",
		output = os.path.join(PLUGIN_DIR, "images", "ocr.jpg"),
		cwd = os.path.join(PLUGIN_DIR, "wia-cmd-scanner")
		)
		p = Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
		stdout, stderr = p.communicate()
		if stderr or stdout == b'No compatible scanners found\r\n':
			raise RuntimeError("Subprocess wia-cmd-scanner failed:\n {error}".format(error=stderr.decode()) if stderr else stdout.decode())

	def showResults(self):
		# Opening the TXT file with OCR results.
		z = ctypes.windll.shell32.ShellExecuteW(None, "open", ocrTxtPath, None, None, 10)

	def deleteFiles(self):
		# Delete the temporary files...
		filePath = "del " + pngFilesPath[:-4] + "*.*\" /q"
		os.system(filePath)
		filePath = "del " + listPath + " /q"
		os.system(filePath)

	def _doRoutines(self):
		# Convert PDF in PNG files compatibles with Tesseract...
		self.convertPDFToPNG()
		# Create the list of PNG files
		self.createList()
		# Perform OCR to all PNG files in the list.txt
		self.OCR_image_files(listPath)

	def _doRoutines1(self):
		# Perform OCR to the selected image file...
		self.OCR_image_files(docPath)

	def _doRoutines2(self):
		# Digitalize page from scanner
		self.digitalizeDocument()
		# Perform OCR to the JPG created...
		jpgFilePath = os.path.join(PLUGIN_DIR, "images", "ocr.jpg")
		global lang, doc
		try:
			lang = config.conf["tesseractOCR"]["language"]
		except KeyError:
			lang = lng
		doc = str(config.conf["tesseractOCR"]["docType"])
		# Wait until file be put on right local
		while not  os.path.exists(jpgFilePath):
			time.sleep(0.01)
		if os.path.exists(jpgFilePath):
			si = subprocess.STARTUPINFO()
			si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			command = "{} {} {} --dpi 300 --psm {} -l {} quiet".format(tesseractPath, jpgFilePath, pngFilesPath, doc, lang)
			p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=si)
			stdout, stderr = p.communicate()
		self.showResults()

	@script( 
		# For translators: Message to be announced during Keyboard Help 
		description = _("Performs OCR to focused file in File Explorer"), 
		category = "TesseractOCR", 
		gesture = "kb:control+windows+r")
	def script_OCRFile(self, gesture):
		# Delete the files from previous OCR
		self.deleteFiles()
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		# Obtain the full path of the selected file
		self.getDocName()
		# Check if is a supported file, and if yes if it is PDF or image file
		ext = docPath[-5:-1].lower()
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
		# Delete the files from previous OCR
		self.deleteFiles()
		ui.message(_("Processing... Please wait... This operation can takes some seconds..."))
		self._thread = threading.Thread(target = self._doRoutines2)
		self._thread.setDaemon(True)
		self._thread.start()

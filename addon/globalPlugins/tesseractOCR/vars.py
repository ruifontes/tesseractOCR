#-*- coding: utf-8 -*-
# Variables for the TesseractOCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Colaboration of Chatt GPT ito list available scanners...
# Copyright (C) 2022-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import os
import wx
import ui
import globalVars
import config
import comtypes.client
import addonHandler

# To start the translation process
addonHandler.initTranslation()

# Location of executables:
PLUGIN_DIR = os.path.dirname(__file__)
tesseractPath = "\""+os.path.join (PLUGIN_DIR, "tesseract", "tesseract.exe")+"\""
pdf2PNGPath = "\""+os.path.join (PLUGIN_DIR, "xpdf-tools", "pdftopng.exe")+"\""
pdf2TextPath = "\""+os.path.join (PLUGIN_DIR, "xpdf-tools", "pdftotext.exe")+"\""

# Supported file types:
suppFiles = ["bmp", "pnm", "pbm", "pgm", "png", "jpg", "jp2", "gif", "tif", "jfif", "jpeg", "tiff", "spix", "webp"]

# Location of files:
pngFilesPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr")+"\""    # Folder where to place the PNG files extracted from the PDF file
listPath = "\""+os.path.join (PLUGIN_DIR, "list.txt")+"\""             # Location of the PNG files list
ocrTxtPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr.txt")+"\""  # Location of the text file with the results
textFilesPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr.txt")+"\"" # Folder where to place the txt file extracted from the PDF file

def initConfiguration():
	confspec = {
		"language" : "string(default="")",
		"docType" : "integer(default=6)",
		"askPassword" : "boolean(default=false)",
		"dpi": "string(default="")",
		"device" : "string(default="")",
	}
	config.conf.spec["tesseractOCR"] = confspec

initConfiguration()

# Variables read from config
# Reading or setting OCR language...
lang = ""
try:
	if config.conf["tesseractOCR"]["language"]:
		lang = config.conf["tesseractOCR"]["language"]
except KeyError:
	lang = "eng"

# Reading or setting OCR doc type...
doc = 3
try:
	if config.conf["tesseractOCR"]["docType"]:
		doc = int(config.conf["tesseractOCR"]["docType"])
except KeyError:
	doc = 3

DOC_OSD = 1
DOC_ALL = 3
DOC_TEXT = 6
DOC_LABELS = {
	# Translators: The entry for various docs,  with auto-orientation...
	DOC_OSD : pgettext("docType", _("With auto-orientation")),
	# Translators: The entry for various types of docs, invoices, bills, magazines and so on...
	DOC_ALL : pgettext("docType", _("Various")),
	# Translators: The entry for text only, like books and letters for instance...
	DOC_TEXT : pgettext("docType", _("Text"))
}
docTypesLabel = (DOC_OSD, DOC_ALL, DOC_TEXT)
docTypesChoices = [DOC_LABELS[Type] for Type in docTypesLabel]

# Reading if is needed to ask PDF password...
try:
	if config.conf["tesseractOCR"]["askPassword"]:
		shouldAskPwd = config.conf["tesseractOCR"]["askPassword"]
except KeyError:
	shouldAskPwd = False

# Reading or setting OCR DPI
try:
	if config.conf["tesseractOCR"]["dpi"]:
		DPI = config.conf["tesseractOCR"]["dpi"]
except KeyError:
	DPI = "300"

dpiList = ["150", "200", "300", "400"]

# Create a list of WIA devices for settings panel
global noScanner
noScanner = False
# Create WIA connection
d = comtypes.client.CreateObject("WIA.DeviceManager")
# Check if WIA devices are present
if not d.DeviceInfos.count:
	noScanner = True
	WIAList = [_("No scanner found")]
else:
	k = d.DeviceInfos.count
	n = 0
	WIAList = [_("No scanner found")]
	for n in range(k):
		WIAList.append(d.DeviceInfos[n+1].Properties["Name"].Value)

# Reading or setting device to use
try:
	if config.conf["tesseractOCR"]["device"]:
		scanner = config.conf["tesseractOCR"]["device"]
except KeyError:
	scanner = WIAList[0]

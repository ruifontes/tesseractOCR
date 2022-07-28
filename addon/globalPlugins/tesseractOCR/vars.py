#-*- coding: utf-8 -*-
# Variables for the TesseractOCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2022 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

import os
import config
# For translation
import addonHandler
addonHandler.initTranslation()

# Location of executables:
PLUGIN_DIR = os.path.dirname(__file__)
tesseractPath = "\""+os.path.join (PLUGIN_DIR, "tesseract", "tesseract.exe")+"\""
pdf2PNGPath = "\""+os.path.join (PLUGIN_DIR, "xpdf-tools", "pdftopng.exe")+"\""
wiaCwd = os.path.join(PLUGIN_DIR, "wia-cmd-scanner")
wiaCMDPath = os.path.join(PLUGIN_DIR, "wia-cmd-scanner", "wia-cmd-scanner.exe")

# Supported file types:
suppFiles = ["bmp", "pnm", "pbm", "pgm", "png", "jpg", "jp2", "gif", "tif", "jfif", "jpeg", "tiff", "spix", "webp"]

# Location of files:
pngFilesPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr")+"\""    # Folder where to place the PNG files extracted from the PDF file
listPath = "\""+os.path.join (PLUGIN_DIR, "list.txt")+"\""             # Location of the PNG files list
jpgFilePath = os.path.join(PLUGIN_DIR, "images", "ocr.jpg")            # Location of JPG file resultant from scanning
ocrTxtPath = "\""+os.path.join (PLUGIN_DIR, "images", "ocr.txt")+"\""  # Location of the text file with the results

# Variables read from config
# Reading or setting OCR language...
try:
	if config.conf["tesseractOCR"]["language"]:
		lang = config.conf["tesseractOCR"]["language"]
except KeyError:
	lang = "eng"

#Reading or setting OCR doc type...
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

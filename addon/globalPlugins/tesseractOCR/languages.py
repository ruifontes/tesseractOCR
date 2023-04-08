#-*- coding: utf-8 -*-
# Language list and construction of language variables for tesseractOCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2022-2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import os
import config
import languageHandler
# For translation
import addonHandler
addonHandler.initTranslation()

# Language codes of NVDA, or customized language name, and Tesseract language codes
localesToTesseractLangs = {
	"af" : "afr",
	"am" : "amh",
	"ar" : "ara",
	"as" : "asm",
	"az" : "aze",
	"be" : "bel",
	"bn" : "ben",
	"bo" : "bod",
	"bs" : "bos",
	"br" : "bre",
	"bg" : "bul",
	"ca" : "cat",
	_("Cebuan") : "ceb",
	"cs" : "ces",
	"zh_CN" : "chi_sim",
	"zh_HK" : "chi_tra",
	"chr" : "chr",
	"co" : "cos",
	"cy" : "cym",
	"da" : "dan",
	"de" : "deu",
	"dv" : "div",
	"dz" : "dzo",
	"el" : "ell",
	"en" : "eng",
	_("Esperanto") : "epo",
	"et" : "est",
	_("Math equations") : "equ",
	"eu" : "eus",
	"fa" : "fas",
	_("Filipino") : "fil",
	"fi" : "fin",
	"fo" : "fao",
	"fr" : "fra",
	"fy" : "fry",
	"gd" : "gla",
	"ga" : "gle",
	"gl" : "glg",
	"gu" : "guj",
	_("Haitian") : "hat",
	"he" : "heb",
	"hi" : "hin",
	"hr" : "hrv",
	"hu" : "hun",
	"id" : "ind",
	"hy" : "hye",
	"iu" : "iku",
	"is" : "isl",
	"it" : "ita",
	_("Javanese") : "jav",
	"ja" : "jpn",
	"kn" : "kan",
	"ka" : "kat",
	"kk" : "kaz",
	"ckb" : "khm",
	"ky" : "kir",
	"kmr" : "kmr",
	"ko" : "kor",
	"lo" : "lao",
	"la" : "lat",
	"lv" : "lav",
	"lt" : "lit",
	"lb" : "ltz",
	"ml" : "mal",
	"mr" : "mar",
	"mt" : "mlt",
	"mk" : "mkd",
	"mn" : "mon",
	"mi" : "mri",
	"ms" : "msa",
	"my" : "mya",
	"ne" : "nep",
	"nl" : "nld",
	"nb_NO" : "nor",
	"oc" : "oci",
	"or" : "ori",
	"pa" : "pan",
	"pl" : "pol",
	"pt" : "por",
	"ps" : "pus",
	"qu" : "que",
	"ro" : "ron",
	"ru" : "rus",
	"sa" : "san",
	"si" : "sin",
	"sk" : "slk",
	"sl" : "slv",
	"sd" : "snd",
	"es" : "spa",
	"sq" : "sqi",
	"sr" : "srp_latn",
	_("Sundanese") : "sun",
	"sw" : "swa",
	"sv" : "swe",
	_("Syriac") : "syr",
	"ta" : "tam",
	"tt" : "tat",
	"te" : "tel",
	"tg" : "tgk",
	"th" : "tha",
	"ti" : "tir",
	_("Tonga") : "ton",
	"tr" : "tur",
	"ug" : "uig",
	"uk" : "ukr",
	"ur" : "urd",
	"uz" : "uzb",
	"vi" : "vie",
	"yi" : "yid",
	"yo" : "yor"
}

# Correspondence between language codes of Tesseract and NVDA
tesseractLangsToLocales = {v : k for k, v in localesToTesseractLangs.items()}

def getAvailableTesseractLanguages():
	# Path of folder containing the .traineddata files responsible for OCR language...
	dataDir = os.path.join(os.path.dirname(__file__), "tesseract", "tessdata")
	# List of files...
	dataFiles = [file for file in os.listdir(dataDir) if file.endswith('.traineddata') and file != "osd.traineddata"]
	# Create a list only with the lang name...
	return [os.path.splitext(file)[0] for file in dataFiles]

# Get the dict of available langs
availableLangs = {languageHandler.getLanguageDescription(tesseractLangsToLocales[lang]) or tesseractLangsToLocales[lang] : lang for lang in list(localesToTesseractLangs.values())}
langsDesc = []
tessLangsToDescs = {v : k  for k, v in availableLangs.items()}
try:
	if config.conf["tesseractOCR"]["language"]:
		# Record exist, so use it...
		langs = config.conf["tesseractOCR"]["language"]
		langs = langs.split("+")
		# Get lang description
		for item in langs:
			item = tessLangsToDescs[item]
			langsDesc.append(item)
except KeyError:
	# Do not exist, so the list is empty
	landsDesc = []
# List of all languages descriptions
lista = list(availableLangs.keys())
# Now removing the languages already selected for OCR use
if len(langsDesc) != 0:
 for item in langsDesc:
		lista.remove(str(item))
else:	
	pass


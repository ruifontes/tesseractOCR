#-*- coding: utf-8 -*-
# Module with language list and construction of language variables for tesseractOCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2022-2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import os
import config
import languageHandler
import addonHandler

# To start the translation process
addonHandler.initTranslation()

# Tesseract language codes and corresponding language codes of NVDA/Windows 
tesseractLangsToLocales = {
	"afr": "af",
	"amh": "am",
	"ara": "ar",
	"asm": "as",
	"aze": "az",
	"bel": "be",
	"ben": "bn",
	"bod": "bo",
	"bos": "bs",
	"bre": "br",
	"bul": "bg",
	"cat": "ca",
	"ceb": None,
	"ces": "cs",
	"chi_sim": "zh_CN",
	"chi_tra": "zh_HK",
	"chr": "chr",
	"cos": "co",
	"cym": "cy",
	"dan": "da",
	"deu": "de",
	"div": "dv",
	"dzo": "dz",
	"ell": "el",
	"eng": "en",
	"epo": None,
	"equ": None,
	"est": "et",
	"eus": "eu",
	"fas": "fa",
	"fil": None,
	"fin": "fi",
	"fao": "fo",
	"fra": "fr",
	"fry": "fy",
	"gla": "gd",
	"gle": "ga",
	"glg": "gl",
	"guj": "gu",
	"hat": None,
	"heb": "he",
	"hin": "hi",
	"hrv": "hr",
	"hun": "hu",
	"ind": "id",
	"hye": "hy",
	"iku": "iu",
	"isl": "is",
	"ita": "it",
	"jav": None,
	"jpn": "ja",
	"kan": "kn",
	"kat": "ka",
	"kaz": "kk",
	"khm": "ckb",
	"kir": "ky",
	"kmr": "kmr",
	"kor": "ko",
	"lao": "lo",
	"lat": "la",
	"lav": "lv",
	"lit": "lt",
	"ltz": "lb",
	"mal": "ml",
	"mar": "mr",
	"mlt": "mt",
	"mkd": "mk",
	"mon": "mn",
	"mri": "mi",
	"msa": "ms",
	"mya": "my",
	"nep": "ne",
	"nld": "nl",
	"nor": "nb_NO",
	"oci": "oc",
	"ori": "or",
	"pan": "pa",
	"pol": "pl",
	"por": "pt",
	"pus": "ps",
	"que": "qu",
	"ron": "ro",
	"rus": "ru",
	"san": "sa",
	"sin": "si",
	"slk": "sk",
	"slv": "sl",
	"snd": "sd",
	"spa": "es",
	"sqi": "sq",
	"srp_latn": "sr",
	"sun": None,
	"swa": "sw",
	"swe": "sv",
	"syr": None,
	"tam": "ta",
	"tat": "tt",
	"tel": "te",
	"tgk": "tg",
	"tha": "th",
	"tir": "ti",
	"ton": None,
	"tur": "tr",
	"uig": "ug",
	"ukr": "uk",
	"urd": "ur",
	"uzb": "uz",
	"vid": "vi",
	"yid": "yi",
	"yor": "yo"
}

# Description of Tesseract language codes for languages that cannot be provided by NVDA/Windows function
additionalLangDesc = {
	"ceb": _("Cebuan"),
	"epo": _("Esperanto"),
	"equ": _("Math equations"),
	"fil": _("Filipino"),
	"hat": _("Haitian"),
	"jav": _("Javanese"),
	"sun": _("Sundanese"),
	"syr": _("Syriac"),
	"ton": _("Tonga"),
}

def getAvailableTesseractLanguages():
	# Path of folder containing the .traineddata files responsible for OCR language...
	dataDir = os.path.join(os.path.dirname(__file__), "tesseract", "tessdata")
	# List of files...
	dataFiles = [file for file in os.listdir(dataDir) if file.endswith('.traineddata') and file != "osd.traineddata"]
	# Create a list only with the lang name...
	return [os.path.splitext(file)[0] for file in dataFiles]

# Get the dict of available langs
def getLanguageDescription(lang):
	"""Get language description from Tesseract language codes"""
	try:
		# First check in the list of languages not well supported by Windows/NVDA
		return additionalLangDesc[lang]
	except KeyError:
		# Normal case: use NVDA's function to get language description
		return languageHandler.getLanguageDescription(tesseractLangsToLocales[lang])
availableLangs = {getLanguageDescription(lang): lang for lang in tesseractLangsToLocales.keys()}
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


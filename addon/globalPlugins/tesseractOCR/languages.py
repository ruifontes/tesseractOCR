#-*- coding: utf-8 -*-
# Module with language list and construction of language variables for tesseractOCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Thanks by Cyrille Bougot colaboration!
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
	"afr": "af", # lang 0
	"amh": "am", # lang 1
	"ara": "ar", # lang 2
	"asm": "as", # lang 3
	"aze": "az", # lang 4
	"bel": "be", # lang 5
	"ben": "bn", # lang 6
	"bod": "bo", # lang 7
	"bos": "bs", # lang 8
	"bre": "br", # lang 9
	"bul": "bg", # lang 10
	"cat": "ca", # lang 11
	"ceb": None, # lang 12
	"ces": "cs", # lang 13
	"chi_sim": "zh_CN", # lang 14
	"chi_tra": "zh_HK", # lang 15
	#"chr": "chr", Removed since introduced only in Windows 8...
	"chr": None, # lang 16
	"cos": "co", # lang 17
	"cym": "cy", # lang 18
	"dan": "da", # lang 19
	"deu": "de", # lang 20
	"div": "dv", # lang 21
	#"dzo": "dz", Removed since introduced only in Windows 8...
	"dzo": None, # lang 22
	"ell": "el", # lang 23
	"eng": "en", # lang 24
	"epo": None, # lang 25
	"equ": None, # lang 26
	"est": "et", # lang 27
	"eus": "eu", # lang 28
	"fas": "fa", # lang 29
	"fil": None, # lang 30
	"fin": "fi", # lang 31
	"fao": "fo", # lang 32
	"fra": "fr", # lang 33
	"fry": "fy", # lang 34
	#"gla": "gd", Removed since introduced only in Windows 8...
	"gla": None, # lang 35
	"gle": "ga", # lang 36
	"glg": "gl", # lang 37
	"guj": "gu", # lang 38
	"hat": None, # lang 39
	"heb": "he", # lang 40
	"hin": "hi", # lang 41
	"hrv": "hr", # lang 42
	"hun": "hu", # lang 43
	"ind": "id", # lang 44
	"hye": "hy", # lang 45
	"iku": "iu", # lang 46
	"isl": "is", # lang 47
	"ita": "it", # lang 48
	"jav": None, # lang 49
	"jpn": "ja", # lang 50
	"kan": "kn", # lang 51
	"kat": "ka", # lang 52
	"kaz": "kk", # lang 53
	"khm": "ckb", # lang 54
	"kir": "ky", # lang 55
	"kmr": "kmr", # lang 56
	"kor": "ko", # lang 57
	"lao": "lo", # lang 58
	#"lat": "la", Removed since is not part of Windows languages
	"lat": None, # lang 59
	"lav": "lv", # lang 60
	"lit": "lt", # lang 61
	"ltz": "lb", # lang 62
	"mal": "ml", # lang 63
	"mar": "mr", # lang 64
	"mlt": "mt", # lang 065
	"mkd": "mk", # lang 66
	"mon": "mn", # lang 67
	"mri": "mi", # lang 068
	"msa": "ms", # lang 69
	"mya": "my", # lang 70
	"nep": "ne", # lang 71
	"nld": "nl", # lang 72
	"nor": "nb_NO", # lang 73
	"oci": "oc", # lang 74
	"ori": "or", # lang 75
	#"pan": "pa", Removed since introduced only in Windows 8...
	"pan": None, # lang 76
	"pol": "pl", # lang 77
	"por": "pt", # lang 78
	"pus": "ps", # lang 79
	#"que": "qu", # Removed since it is not in Windows 7
	"que": None, # lang 80
	"ron": "ro", # lang 81
	"rus": "ru", # lang 82
	"san": "sa", # lang 83
	"sin": "si", # lang 84
	"slk": "sk", # lang 85
	"slv": "sl", # lang 86
	#"snd": "sd", Removed since introduced only in Windows 8...
	"snd": None, # lang 87
	"spa": "es", # lang 88
	"sqi": "sq", # lang 89
	"srp_latn": "sr", # lang 90
	"sun": None, # lang 91
	"swa": "sw", # lang 92
	"swe": "sv", # lang 93
	"syr": None, # lang 94
	"tam": "ta", # lang 95
	"tat": "tt", # lang 96
	"tel": "te", # lang 97
	"tgk": "tg", # lang 98
	"tha": "th", # lang 99
	#"tir": "ti", Removed since introduced only in Windows 8...
	"tir": None, # lang 100
	"ton": None, # lang 101
	"tur": "tr", # lang 102
	#"uig": "ug", Removed since introduced only in Windows 8...
	"uig": None, # lang 103
	"ukr": "uk", # lang 104
	"urd": "ur", # lang 105
	"uzb": "uz", # lang 106
	"vid": "vi", # lang 107
	#"yid": "yi", Removed since it is not in Windows 7
	"yid": None, # lang 108
	"yor": "yo" # lang 109
}

# Description of Tesseract language codes for languages that cannot be provided by NVDA/Windows function
# Code contributed by Cyrille Bougot
additionalLangDesc = {
	"ceb": _("Cebuan"),
	"chr": _("Cherokee"),
	"dzo": "Dzongkha",
	"epo": _("Esperanto"),
	"equ": _("Math equations"),
	"fil": _("Filipino"),
	"gla": _("Scottish Gaelic"),
	"hat": _("Haitian"),
	"jav": _("Javanese"),
	"lat": _("Latin"),
	"pan": _("Punjabi"),
	"que": _("Quechua"),
	"snd": _("Sindhi"),
	"sun": _("Sundanese"),
	"syr": _("Syriac"),
	"tir": _("Tigrinya"),
	"ton": _("Tonga"),
	"uig": _("Uyghur"),
	"yid": _("Yiddish"),
}

def getAvailableTesseractLanguages():
	# Path of folder containing the .traineddata files responsible for OCR language...
	dataDir = os.path.join(os.path.dirname(__file__), "tesseract", "tessdata")
	# List of files...
	dataFiles = [file for file in os.listdir(dataDir) if file.endswith('.traineddata') and file != "osd.traineddata"]
	# Create a list only with the lang name...
	return [os.path.splitext(file)[0] for file in dataFiles]

# Get the dict of available langs
# Code contributed by Cyrille Bougot
def getLanguageDescription(lang):
	# Get language description from Tesseract language codes
	try:
		# First check in the list of languages not well supported by Windows/NVDA
		return additionalLangDesc[lang]
	except KeyError:
		# Normal case: use NVDA's function to get language description
		return languageHandler.getLanguageDescription(tesseractLangsToLocales[lang])
availableLangs = {getLanguageDescription(lang): lang for lang in tesseractLangsToLocales.keys()}
# End code contributed by Cyrille Bougot

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

#-*- coding: utf-8 -*-
# Part of tesseractOCR add-on for NVDA.
# Module to preserve the downloaded trainedData files
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import os
import shutil
import globalVars
import addonHandler

def onInstall():
	configFilePath = os.path.abspath(os.path.join(globalVars.appArgs.configPath, "addons", "tesseractOCR", "globalPlugins", "tesseractOCR", "tesseract", "tessdata"))
	if os.path.isdir(configFilePath):
		shutil.rmtree(os.path.abspath(os.path.join(globalVars.appArgs.configPath, "addons", "tesseractOCR" + addonHandler.ADDON_PENDINGINSTALL_SUFFIX, "globalPlugins", "tesseractOCR", "tesseract", "tessdata")))
		os.rename(configFilePath, os.path.abspath(os.path.join(globalVars.appArgs.configPath, "addons", "tesseractOCR" + addonHandler.ADDON_PENDINGINSTALL_SUFFIX, "globalPlugins", "tesseractOCR", "tesseract", "tessdata")))

#-*- coding: utf-8 -*-
# Code for create a config panel in NVDA settings for tesseractOCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2020-2022 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

import gui
import wx
import config
import functools
from configobj import ConfigObj
#import languageHandler
import threading
# For update process
from .update import *
# For translation
import addonHandler
addonHandler.initTranslation()

from . import runInThread
lista = []
langsDesc = []
docTypesChoices = []
lang = ""
doc = 3
from .languages import lista, langsDesc, availableLangs, getAvailableTesseractLanguages
from .vars import PLUGIN_DIR, docTypesChoices, docTypesLabel, doc, DOC_OSD, DOC_ALL, DOC_TEXT, lang

initConfiguration()


class OCRSettingsPanel(gui.SettingsPanel):
	# Translators: Title of the OCR settings dialog in the NVDA settings.
	title = "TesseractOCR"

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer = settingsSizer)
		self.onMoveUp = functools.partial(self.onMove, -1)
		self.onMoveDown = functools.partial(self.onMove, 1)

		# Translators: Label of a  combobox used to choose a recognition language
		recogLanguageLabel = _("Available recognition &language")
		self.recogLanguageCB = sHelper.addLabeledControl(
			recogLanguageLabel,
			wx.Choice,
			choices = lista,
			style = wx.CB_SORT
		)
		# Set selection to the first item
		self.recogLanguageCB.SetSelection(0)

		self.addButton = sHelper.addItem(wx.Button(self, label = _("&Add"), name="Add"))
		self.addButton.Bind(wx.EVT_BUTTON, self.onAdd)

		# Translators: Name of a list with the languages selected for OCR use
		self.enabledLangs = sHelper.addLabeledControl(_("Selected languages"), wx.ListBox, choices = langsDesc, style = wx.LB_SINGLE)
		if len(self.enabledLangs.Items) != 0:
			self.enabledLangs.SetSelection(0)
		self.enabledLangs.Bind(wx.EVT_LISTBOX, self.onChange)
		self.enabledLangs.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)

		self.removeButton = sHelper.addItem(wx.Button(self, label = _("&Remove"), name="Remove"))
		self.removeButton.Bind(wx.EVT_BUTTON, self.onRemove)

		self.moveUpButton = sHelper.addItem(wx.Button(self, label = _("Move &up"), name = "Up"))
		self.moveUpButton.Bind(wx.EVT_BUTTON, self.onMoveUp)

		self.moveDownButton = sHelper.addItem(wx.Button(self, label = _("Move &down"), name = "Down"))
		self.moveDownButton.Bind(wx.EVT_BUTTON, self.onMoveDown)

		self.updateControls()

		# Translators: Label of a  combobox used to choose a type of document to recognize
		recogDocTypeLabel = _("&Type of document")
		self.recogDocTypeCB = sHelper.addLabeledControl(
			recogDocTypeLabel,
			wx.Choice,
			choices = list(docTypesChoices),
			style = wx.CB_SORT
		)
		self.recogDocTypeCB.SetSelection(docTypesLabel.index(doc))

		# Translators: Checkbox name in the configuration dialog
		self.shouldUpdateChk = sHelper.addItem(wx.CheckBox(self, label=_("Check for updates at startup")))
		self.shouldUpdateChk.SetValue(config.conf[ourAddon.name]["isUpgrade"])
		if config.conf.profiles[-1].name:
			self.shouldUpdateChk.Disable()

	def onAdd(self, evt):
		self.swapItems(evt, self.recogLanguageCB, self.enabledLangs)

	def onRemove(self, evt):
		self.swapItems(evt, self.enabledLangs, self.recogLanguageCB)

	def swapItems(self, evt, source, target):
		index = source.GetSelection()
		if index == -1:
			return
		target.Append(source.GetString(index))
		target.SetSelection(0)
		source.Delete(index)
		if len(source.Items) > 0:
			source.SetFocus()
			source.SetSelection(index if index < source.Count - 1 else index - 1)
		self.updateControls()

	def onMove(self, direction, evt):
		curIndex = self.enabledLangs.GetSelection()
		if curIndex == -1:
			return
		if direction == -1 and curIndex == 0 or direction == 1 and curIndex == self.enabledLangs.Count - 1:
			return
		newIndex = curIndex + direction
		curItem = self.enabledLangs.GetString(curIndex)
		newItem = self.enabledLangs.GetString(newIndex)
		self.enabledLangs.SetString(curIndex, newItem)
		self.enabledLangs.SetString(newIndex, curItem)
		self.enabledLangs.SetFocus()
		self.enabledLangs.SetSelection(newIndex)
		self.updateControls()

	def onKeyDown(self, evt):
		if evt.KeyCode == wx.WXK_UP and evt.controlDown:
					self.onMoveUp(evt)
		elif evt.KeyCode == wx.WXK_DOWN and evt.controlDown:
					self.onMoveDown(evt)
		else:
			evt.Skip()

	def onChange(self, evt):
		self.updateControls()

	def updateControls(self):
		# possibly adding temporary class fields to eliminate unnnecessary computations.
		index = self.enabledLangs.GetSelection()
		self.moveUpButton.Disable() if index == 0 or index == -1 else self.moveUpButton.Enable()
		self.moveDownButton.Disable() if index == self.enabledLangs.Count -1 or index == -1 else self.moveDownButton.Enable()
		self.addButton.Disable() if len(self.recogLanguageCB.Items) == 0 else self.addButton.Enable()
		self.removeButton.Disable() if len(self.enabledLangs.Items) == 0 else self.removeButton.Enable()

	def onSave (self):
		global lista, langsDesc, lang, doc
		lista = self.recogLanguageCB.Items
		langsDesc = self.enabledLangs.Items
		lang = ""
		n = 0
		while n < len(langsDesc):
			if n == 0:
				lang += availableLangs[langsDesc[n]]
			else:
				lang = lang + "+" + availableLangs[langsDesc[n]]
			n += 1
		config.conf["tesseractOCR"]["language"] = lang

		doc = docTypesChoices[self.recogDocTypeCB.GetSelection()]
		if doc == pgettext("docType", _("Text")):
			doc = 6
		elif doc == pgettext("docType", _("Various")):
			doc = 3
		else:
			doc = 1
		config.conf["tesseractOCR"]["docType"] = doc

		if not config.conf.profiles[-1].name:
			config.conf[ourAddon.name]["isUpgrade"] = self.shouldUpdateChk.GetValue()

		# Routine to download the files to the right folder...
		# Get the language name of file to download
		self.ocrLangs = self.enabledLangs.Items
		self.listAvailable = getAvailableTesseractLanguages()
		self._downloadThread = threading.Thread(target = self._download)
		self._downloadThread.setDaemon(True)
		self._downloadThread.start()

	def _download(self):
		self.doDownload = runInThread.RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
		self.doDownload.start()
		for lang in self.ocrLangs:
			lang = availableLangs[lang]
			if lang not in self.listAvailable:
				ocrLang = lang
				# Construct the name of file to download
				urlN = ocrLang + ".traineddata"
				# Online repository of files
				urlRepos = "https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/"
				# Full URL of the language file...
				urlName = urlRepos + urlN
				# Full path where to save the file
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
			else:
				pass
		self.doDownload.stop()

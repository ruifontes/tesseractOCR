#-*- coding: utf-8 -*-
# Module for settings panel of Tesseract OCR add-on
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Copyright (C) 2022-2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
from .runInThread import *
from .vars import *
import urllib.request
import json
import gui
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel
from gui import guiHelper
import functools

# To start the translation process
addonHandler.initTranslation()

lista = []
langsDesc = []
docTypesChoices = []
lang = ""
doc = 3
shouldAskPwd = False
DPI = "300"
from .languages import lista, langsDesc, availableLangs, getAvailableTesseractLanguages
from .vars import PLUGIN_DIR, docTypesChoices, docTypesLabel, doc, DOC_OSD, DOC_ALL, DOC_TEXT, DPI, dpiList, lang

initConfiguration()


class OCRSettingsPanel(gui.SettingsPanel):
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

		# Translators: Label of a  button used to add more recognition languages
		self.addButton = sHelper.addItem(wx.Button(self, label = _("&Add"), name="Add"))
		self.addButton.Bind(wx.EVT_BUTTON, self.onAdd)

		# Translators: Name of a list with the languages selected for OCR use
		self.enabledLangs = sHelper.addLabeledControl(_("Selected languages"), wx.ListBox, choices = langsDesc, style = wx.LB_SINGLE)
		# Set selection to the first item if some are present
		if len(self.enabledLangs.Items) != 0:
			self.enabledLangs.SetSelection(0)
		self.enabledLangs.Bind(wx.EVT_LISTBOX, self.onChange)
		self.enabledLangs.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)

		# Translators: Label of a  button used to remove a recognition language
		self.removeButton = sHelper.addItem(wx.Button(self, label = _("&Remove"), name="Remove"))
		self.removeButton.Bind(wx.EVT_BUTTON, self.onRemove)

		# Translators: Label of a  button used to move up a recognition language
		self.moveUpButton = sHelper.addItem(wx.Button(self, label = _("Move &up"), name = "Up"))
		self.moveUpButton.Bind(wx.EVT_BUTTON, self.onMoveUp)

		# Translators: Label of a  button used to move down a recognition language
		self.moveDownButton = sHelper.addItem(wx.Button(self, label = _("&Move down"), name = "Down"))
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
		# Set selection to the item set in configurations
		self.recogDocTypeCB.SetSelection(docTypesLabel.index(doc))

		# Translators: Label of a  combobox used to choose the device  to be used to digitalize
		deviceLabel = _("&Scanner:")
		self.deviceCB = sHelper.addLabeledControl(
			deviceLabel,
			wx.Choice,
			choices = WIAList,
			style = 0
		)
		# Set selection to the item set in configurations
		from .vars import noScanner, scanner
		if noScanner == True:
			scanner = _("No scanner found")
		self.deviceCB.SetSelection(WIAList.index(scanner))

		# Translators: Label of a  combobox used to choose a value for DPI used to digitalize from scanner
		dpiLabel = _("Resolution in &DPI")
		self.dpiCB = sHelper.addLabeledControl(
			dpiLabel,
			wx.Choice,
			choices = dpiList,
			style = wx.CB_SORT
		)
		# Set selection to the item set in configurations
		self.dpiCB.SetSelection(dpiList.index(DPI))

		# Translators: Name  of a checkbox in the configuration dialog ask or not for a password
		self.askPwd = sHelper.addItem(wx.CheckBox(self, label=_("Ask for password")))
		self.askPwd.SetValue(bool(config.conf["tesseractOCR"]["askPassword"]))

	def onAdd(self, evt):
		# Move the language add to the enabled languages list
		self.swapItems(evt, self.recogLanguageCB, self.enabledLangs)

	def onRemove(self, evt):
		# Remove the language removed  from the enabled languages list
		self.swapItems(evt, self.enabledLangs, self.recogLanguageCB)

	def swapItems(self, evt, source, target):
		# Moving languages from one list to the other...
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
		global lista, langsDesc, lang, doc, DPI,scanner,  shouldAskPwd
		# Get OCR languages
		lista = self.recogLanguageCB.Items
		langsDesc = self.enabledLangs.Items
		lang = ""
		lang = "+".join(availableLangs[l] for l in langsDesc)
		config.conf["tesseractOCR"]["language"] = lang

		# Get OCR doc types
		doc = docTypesChoices[self.recogDocTypeCB.GetSelection()]
		if doc == pgettext("docType", _("Text")):
			doc = 6
		elif doc == pgettext("docType", _("Various")):
			doc = 3
		else:
			doc = 1
		config.conf["tesseractOCR"]["docType"] = doc

		# Get the need of asking for a password
		shouldAskPwd = self.askPwd.GetValue()
		config.conf["tesseractOCR"]["askPassword"] = shouldAskPwd

		# Get device to use
		scanner = WIAList[self.deviceCB.GetSelection()]
		config.conf["tesseractOCR"]["device"] = scanner

		# Get OCR DPI resolution
		DPI = dpiList[self.dpiCB.GetSelection()]
		config.conf["tesseractOCR"]["dpi"] = DPI

		# Reactivate profiles triggers
		config.conf.enableProfileTriggers()
		self.Hide()

		# Routine to download the files to the right folder...
		# Get the language name of file to download
		self.ocrLangs = self.enabledLangs.Items
		self.listAvailable = getAvailableTesseractLanguages()
		self._downloadThread = threading.Thread(target = self._download)
		self._downloadThread.setDaemon(True)
		self._downloadThread.start()

	def onPanelActivated(self):
		# Deactivate all profile triggers and active profiles
		config.conf.disableProfileTriggers()
		self.Show()

	def onPanelDeactivated(self):
		# Reactivate profiles triggers
		config.conf.enableProfileTriggers()
		self.Hide()

	def _download(self):
		self.doDownload = RepeatBeep(delay=2.0, beep=(200, 200), isRunning=None)
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
				filepath = os.path.join(os.path.dirname(__file__), "tesseract", "tessdata")
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

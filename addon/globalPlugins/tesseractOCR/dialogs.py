# -*- coding:utf-8 -*-
# File with dialogs for tesseractOCR add-on
# Copyright (C) 2022 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import globalPluginHandler
import globalVars
import wx
import gui
from gui import guiHelper
import ui
import threading
# For update process
from .update import *
import addonHandler
addonHandler.initTranslation()


class Password(wx.Dialog):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetTitle(_("TesseractOCR"))

		sizer_1 = wx.BoxSizer(wx.VERTICAL)

		# Translators: Asking user to enter the PDF password
		label_1 = wx.StaticText(self, wx.ID_ANY, _("Enter your password"))
		sizer_1.Add(label_1, 0, 0, 0)

		self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
		self.text_ctrl_1.SetFocus()
		sizer_1.Add(self.text_ctrl_1, 0, 0, 0)

		sizer_2 = wx.StdDialogButtonSizer()
		sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

		self.button_OK = wx.Button(self, wx.ID_OK, "")
		self.button_OK.SetDefault()
		sizer_2.AddButton(self.button_OK)

		self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
		sizer_2.AddButton(self.button_CANCEL)

		sizer_2.Realize()

		self.SetSizer(sizer_1)
		sizer_1.Fit(self)

		self.SetAffirmativeId(self.button_OK.GetId())
		self.SetEscapeId(self.button_CANCEL.GetId())

		self.Layout()
		self.CentreOnScreen()

		self.Bind(wx.EVT_TEXT_ENTER, self.onOkButton, self.text_ctrl_1)
		self.Bind(wx.EVT_BUTTON, self.onOkButton, self.button_OK)

	def onOkButton(self, event):
		global pwd
		pwd = self.text_ctrl_1.GetValue()
		self.Destroy()
		# Starting the PDF recognition process
		self.recogPDF = threading.Thread(target = GlobalPlugin._doRoutines)
		self.recogPDF.setDaemon(True)
		self.recogPDF.start()
		event.Skip()


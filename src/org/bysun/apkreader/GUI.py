# -*- coding: UTF-8 -*-
#Boa:Frame:Frame1

import wx
import Main
from os import path
import sys


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CHOOSEBTN, wxID_FRAME1CLOSEBTN, wxID_FRAME1PATHTEXT, 
 wxID_FRAME1STARTBTN, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(377, 361), size=wx.Size(308, 127),
              style=wx.DEFAULT_FRAME_STYLE, title='choose folder')
        self.SetClientSize(wx.Size(300, 100))

        self.chooseBtn = wx.Button(id=wxID_FRAME1CHOOSEBTN, label='...',
              name='chooseBtn', parent=self, pos=wx.Point(272, 16),
              size=wx.Size(19, 24), style=0)
        self.chooseBtn.Bind(wx.EVT_LEFT_DOWN, self.OnChooseBtnRightDown)

        self.startBtn = wx.Button(id=wxID_FRAME1STARTBTN, label='start',
              name='startBtn', parent=self, pos=wx.Point(32, 64),
              size=wx.Size(75, 24), style=0)
        self.startBtn.Enable(False)
        self.startBtn.Bind(wx.EVT_LEFT_DOWN, self.OnStartBtnRightDown)

        self.closeBtn = wx.Button(id=wxID_FRAME1CLOSEBTN, label='close',
              name='closeBtn', parent=self, pos=wx.Point(189, 64),
              size=wx.Size(75, 24), style=0)
        self.closeBtn.Bind(wx.EVT_LEFT_DOWN, self.OnCloseBtnRightDown)

        self.pathText = wx.TextCtrl(id=wxID_FRAME1PATHTEXT, name='pathText',
              parent=self, pos=wx.Point(8, 16), size=wx.Size(256, 22), style=0,
              value='')
        self.pathText.SetEditable(False)

    def __init__(self, parent):
        self.selectedPath = ''
        self._init_ctrls(parent)

    def OnChooseBtnRightDown(self, event):
        dialog = wx.DirDialog(None, "Choose a folder:",
              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            pathStr = dialog.GetPath()+path.sep
            self.pathText.SetValue(pathStr)
            self.pathText.SetToolTipString(pathStr)
            self.selectedPath = pathStr
            self.startBtn.Enable(True)
        dialog.Destroy()

    def OnStartBtnRightDown(self, event):
        Main.process(self.selectedPath)
        self.closeApp()
        

    def OnCloseBtnRightDown(self, event):
        self.closeApp()
        
    def closeApp(self):
        self.Destroy()
        sys.exit(0)

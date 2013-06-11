#!/usr/bin/env python
# TODO: Change TODO Layout to match others
# TODO: Add in Python Remote
# TODO: Integrate event handlers
# TODO: Put in Buttons
# TODO: Add docstrings for the frames

import wx

class App(wx.App):
    """docstring for App"""
    def OnInit(self):
        startFrame = WelcomeFrame()
        startFrame.Show()
        return True

class WelcomeFrame(wx.Frame):
    """docstring for Welcome Frame"""
    def __init__(self):
        self.frame = wx.Frame.__init__(self, parent=None, id=-1, title='Welcome', size=(300, 500))
        self.panel = wx.Panel(self)
        # Creating Menu For File
        self.menubar = wx.MenuBar()
        menuFile = wx.Menu()
        menuEdit = wx.Menu()
        self.CreateMenuItems(menuFile, self.MenuFileData)
        self.CreateMenuItems(menuEdit, self.MenuEditData)
        self.menubar.Append(menuFile, '&File')
        self.menubar.Append(menuEdit, '&Edit')
        self.SetMenuBar(self.menubar)

    def OnClose(self, event):
        self.Close()

    def CreateMenuItems(self, menu, data):
        for label in data():
            menu.Append(wx.NewId(), label)

    def MenuFileData(self):
        return ('New', 'Save', 'Load', 'Exit')

    def MenuEditData(self):
        return ('Edit Connection', 'Edit Keys', 'Connect')

if __name__ == '__main__':
    app = App()
    app.MainLoop()

#!/usr/bin/env python
# TODO: Change TODO Layout to match others
# TODO: Add in Python Remote
# TODO: Put in Buttons
# TODO: Add docstrings for the frames

import wx


class ConnectionConfigBase(wx.Dialog):
    """docstring for ConnectionConfigBase"""
    def __init__(self, parent):
        self.dialog = wx.Dialog.__init__(self, parent=parent, id=-1, title='Testing', size=(300, 300))
        self.panel = wx.Panel(self, size=(300, 300))
        label_1 = wx.StaticText(self.panel, -1, 'tvtype', (10, 10))
        label_2 = wx.StaticText(self.panel, -1, 'mac', (10, 30))
        label_3 = wx.StaticText(self.panel, -1, 'tvip', (10, 50))

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
        self.dictionary = self.PopUpBoxData()
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
            temp = menu.Append(wx.NewId(), label[0])
            self.Bind(wx.EVT_MENU, label[1], temp)

    def MenuFileData(self):
        return (('New', self.OnNew), ('Save', self.OnSave), ('Load', self.OnLoad), ('Exit', self.OnClose))

    def MenuEditData(self):
        return (('Edit Connection', self.OnEdit), ('Edit Keys', self.OnEditC), ('Connect', self.OnConnect))

    def PopUpBoxData(self):
        return {'Save': 'Connection Saved', 'Load': 'Configuration Loaded',
                'Connect': 'Connected'}

    def OnConnect(self, event):
        wx.MessageBox(self.dictionary['Connect'], 'Connect',
                      wx.OK | wx.ICON_INFORMATION)

    def OnSave(self, event):
        wx.MessageBox(self.dictionary['Save'], 'Save',
                      wx.OK | wx.ICON_INFORMATION)

    def OnLoad(self, event):
        wx.MessageBox(self.dictionary['Load'], 'Load',
                      wx.OK | wx.ICON_INFORMATION)

    def OnNew(self, event):
        dlg = ConnectionConfigBase(self.frame)
        dlg.ShowModal()
        dlg.Destroy()

    def OnEdit(self, event):
        print 'Place Holder'

    def OnEditC(self, event):
        print 'Place Holder'

if __name__ == '__main__':
    app = App()
    app.MainLoop()

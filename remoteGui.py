'''
Author: Mohammad Al Faiyaz
Description: This module will be the GUI for the Samsung Remote application. The GUI is being built with
the wxPython toolkit. This module requires Python 2.7.x and the respective wxPython installation.
'''

#!/usr/bin/env python
#-----------------------------------------
# TODO:
'''
* Integrate Python Remote Class
* Put in Buttons
* Organize and refactor ConnectionConfigBase
* Figure out a way to refactor the message dialog part
* Figure out how to initialize python remote with returned data
'''

import wx
import remote


class ConnectionConfigBase(wx.Dialog):
    '''The dialog box for inputing connection details'''
    def __init__(self, parent):
        self.dialog = wx.Dialog.__init__(self, parent=parent, id=-1, title='Testing', size=(300, 300))
        self.InitUI()

    def InitUI(self):
        self.CreateButtons(50)
        self.CreateText(10)
        self.textfields = self.CreateTextCtrl(50)

    def OnCancel(self, event):
        self.Close()

    def OnOk(self, event):
        for i in self.textfields:
            print i.GetValue()
        self.Close()

    def CreateText(self, xdis):
        for i in self.TextData():
            wx.StaticText(self, -1, i[0], (xdis, i[1]))

    def CreateTextCtrl(self, xdis):
        textfields = []
        for i in self.TextCtrlData():
            textfields.append(wx.TextCtrl(self, -1, '', (xdis, i)))
        return textfields

    def CreateButtons(self, xdis):
        for buttons in self.ButtonData():
            temp = wx.Button(self, -1, buttons[0], pos=(xdis, 220))
            self.Bind(wx.EVT_BUTTON, buttons[1], temp)
            xdis += 100

    def TextCtrlData(self):
        return (10, 40, 70)  # returns the y value for the 3 text entry fields

    def ButtonData(self):
        return (('Ok', self.OnOk), ('Cancel', self.OnCancel))

    def TextData(self):
        return (('tvtype', 10), ('mac', 40), ('tvip', 70))


class App(wx.App):
    """The App class for the program"""
    def OnInit(self):
        startFrame = WelcomeFrame()
        startFrame.Show()
        return True


class WelcomeFrame(wx.Frame):
    """The Main/TopFrame for the application. Contains the remote buttons and toolbar menu"""

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

    #  See if you can refactor these 3 methods

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

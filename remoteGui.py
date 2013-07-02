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
* Figure out a way to refactor the message dialog part
* Instead of textfield try to make into list for tvtype
* Cleanup WelcomeFrame
* Welcome frame dictionary/PopUpBoxData cleanup
* Elegant way to bind Button Function
* Make sendkey a modular design
* Testing Linux push capabilities
'''

import wx
import remote


class RemoteModel(remote.Remote):
    """docstring for RemoteModel"""
    def __init__(self):
        remote.Remote.__init__(self, '', '', '')
        self.flag = False

    def InitConnection(self, tvtype, mac, tvip):
        self._tvip = tvip
        self._tvtype = tvtype
        self._mac = mac
        self.flag = True


class ConnectionConfigBase(wx.Dialog):
    '''The dialog box for inputing connection details'''
    def __init__(self, parent):
        self.dialog = wx.Dialog.__init__(self, parent=parent, id=-1, title='Testing', size=(300, 300))
        self.TxtFieldData = []
        self.InitUI()

    def InitUI(self):
        self.CreateButtons(50)
        self.CreateText(10)
        self.textfields = self.CreateTextCtrl(50)

    def GetTxtFieldData(self):
        return self.TxtFieldData

    def OnCancel(self, event):
        self.Close()

    def OnOk(self, event):
        for i in self.textfields:
            self.TxtFieldData.append(i.GetValue())
        self.Close()

    def CreateText(self, xdis):
        for i in self.TextData():
            wx.StaticText(self, -1, i[0], (xdis, i[1]))

    def CreateTextCtrl(self, xdis):
        textfields = []
        for i in self.TextCtrlData():
            textfields.append(wx.TextCtrl(self, -1, '', (xdis, i)))
        return textfields  # Return list for text field reference

    def CreateButtons(self, xdis):
        for buttons in self.ButtonData():
            temp = wx.Button(self, -1, buttons[0], pos=(xdis, 220))
            self.Bind(wx.EVT_BUTTON, buttons[1], temp)
            xdis += 100

    def TextCtrlData(self):
        return (10, 40, 70)  # returns the y value for the text entry fields

    def ButtonData(self):
        return (('Ok', self.OnOk), ('Cancel', self.OnCancel))  # Returns button label and corresponding event handler

    def TextData(self):
        return (('tvtype', 10), ('mac', 40), ('tvip', 70))  # Returns TextData with label and vertical position/text is aligned from same x distance from origin


class App(wx.App):
    """The App class for the program"""
    def OnInit(self):
        startFrame = WelcomeFrame()
        startFrame.Show()
        return True


class WelcomeFrame(wx.Frame):
    """The Main/TopFrame for the application. Contains the remote buttons and toolbar menu"""

    def __init__(self):
        self.frame = wx.Frame.__init__(self, parent=None, id=-1, title='Welcome', size=(190, 660))
        self.panel = wx.Panel(self)
        self.dictionary = self.PopUpBoxData()  # Is this necessary?
        # Creating Menu For File
        self.menubar = wx.MenuBar()
        self.NumButton = []
        self.InitUI()
        self.model = RemoteModel()

    def InitUI(self):
        menuFile = wx.Menu()
        menuEdit = wx.Menu()
        self.CreateMenuItems(menuFile, self.MenuFileData)
        self.CreateMenuItems(menuEdit, self.MenuEditData)
        self.menubar.Append(menuFile, '&File')
        self.menubar.Append(menuEdit, '&Edit')
        self.SetMenuBar(self.menubar)
        self.CreateButtons()

    def OnClose(self, event):
        self.Close()

    def CreateMenuItems(self, menu, data):
        for label in data():
            temp = menu.Append(wx.NewId(), label[0])
            self.Bind(wx.EVT_MENU, label[1], temp)

    def CreateButtons(self):
        pow = wx.Button(self.panel, -1, 'Pow', pos=(5, 5), size=(50, 50))
        src = wx.Button(self.panel, -1, 'Src', pos=(115, 5), size=(50, 50))
        ts = self.ButtonData()
        self.CreateNumButtons()

    def CreateNumButtons(self):
        posis = (5, 60)
        for i in range(9):
            num = i + 1
            self.NumButton.append(wx.Button(self.panel, -1, str(num), pos=posis, size=(50, 50)))
            x, y = posis
            if x < 115:
                x += 55
            else:
                x = 5
                if y < 170:
                    y = y + 55
            posis = (x, y)

    def ButtonData(self):
        return ('Mute', '0', 'Pre',
                'Smart', 'UpArw', 'Tools',
                '<-', 'E', '->',
                'Ret', 'DwnArw', 'Exit',
                'A', 'B', 'C',
                'UpCh', 'D', 'UpVol',
                'DowCh', 'Fav', 'DowCh',
                '<<', '||', '>>',
                'Rec', 'Play', 'Stop')

    def MenuFileData(self):
        return (('New', self.OnNew), ('Save', self.OnSave), ('Load', self.OnLoad), ('Exit', self.OnClose))  # Menu Item label, event handler

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
        initdata = dlg.GetTxtFieldData()
        self.model.InitConnection(initdata[0], initdata[1], initdata[2])
        dlg.Destroy()

    def OnEdit(self, event):
        print 'Place Holder'

    def OnEditC(self, event):
        print 'Place Holder'

if __name__ == '__main__':
    app = App()
    app.MainLoop()

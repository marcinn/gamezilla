# author: Marcin Matląg <marcin.matlag@gmail.com>

from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.DialogBox import DialogBox

from pyjamas.ui.DockPanel import DockPanel

from pyjamas.ui.TextBox import TextBox

from ZillaWindow import ZillaWindow


class  LoginWindow (DialogBox, ZillaWindow):

    def __init__ (self, **kwargs):
        ZillaWindow.__init__(self, kwargs)
        DialogBox.__init__(self, kwargs)
        self.dockPanel = DockPanel()
        self.dockPanel.setSpacing(4)

        self.setText ("Logowanie")

        hpanel1 = HorizontalPanel()
        
        login = TextBox()
        login.setText("Login")
        #hpanel1.add(login)

        passwd = TextBox()
        passwd.setText("Hasło")

        self.dockPanel.add(login, DockPanel.NORTH)
        self.dockPanel.add(passwd, DockPanel.NORTH)

        #hpanel1.add(passwd)

        #self.add(hpanel1)

        self.add(login)
        self.add(passwd)

    def login(self):
        return True

    def join_game (self):
        return True

    def quit (self):
        return True

# author: Marcin Matląg <marcin.matlag@gmail.com>

import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Panel import Panel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.TabPanel import TabPanel

from ZillaWindow import ZillaWindow


class  MainWindow (FocusPanel, ZillaWindow):

    def __init__ (self, **kwargs):
        ZillaWindow.__init__(self, kwargs)
        FocusPanel.__init__(self, kwargs)





    def login(self):
        return True

    def join_game (self):
        return True

    def quit (self):
        return True

# author: Marcin Matląg <marcin.matlag@gmail.com>

from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.TabPanel import TabPanel



from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.Label import Label


from ZillaWindow import ZillaWindow


class  MainWindow (FocusPanel, ZillaWindow):
    """MainWindow class"""

    def __init__ (self, **kwargs):
        ZillaWindow.__init__(self, kwargs)
        FocusPanel.__init__(self, kwargs)

        hpanel1 = HorizontalPanel()

        # menu bar
        main_menu = MenuBar()
        hpanel1.add(main_menu_bar)

        label1 = Label()
        label1.setText("LOL")

        main_menu.add(label1)

        area1 = TextArea()
        area1.setText("Zakładka 1")

        area2 = TextArea()
        area2.setText("Zakładka 2")

        area3 = TextArea()
        area3.setText("Zakładka 2")

        tabs = TabPanel()
        tabs.add(area2, tabText="Gra nr 1")
        tabs.add(area1, tabText="Pokój gier")
        tabs.add(area3, tabText="Pokój gier")

        hpanel1.add(tabs)

        self.add (hpanel1)


    def get_open_games(self):
        return True

    def join_game (self):
        return True

    def quit (self):
        return True

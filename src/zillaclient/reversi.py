# author: Marcin Matląg <marcin.matlag@gmail.com>



import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Panel import Panel
from pyjamas.ui.HTML import HTML

class  MainWindow (Panel):

    def __init__ (self):
        self.setSize("100%", "100%")
        self.setTitle ("Hello World!")


    def get_open_games(self):
        return True

    def join_game (self):
        return True

    def quit (self):
        return True


if __name__ == '__main__':
    pyjd.setup("public/zillaclient.html")
    panel = MainWindow()
    RootPanel().add(panel)
    RootPanel().setTitle("Hello World!")
    RootPanel().add( HTML("""Created by Zilla Team"""))
    
    pyjd.run()



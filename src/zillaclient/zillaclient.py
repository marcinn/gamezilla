# author: Marcin Matląg <marcin.matlag@gmail.com>

import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Panel import Panelfrom pyjamas.ui.HTML import HTML

from MainWindow import MainWindow

#PARAMS

URL = "http://zillagames.pl/service"

if __name__ == '__main__':
    pyjd.setup("public/zillaclient.html")
    t = MainWindow(url=URL)
    RootPanel().add(t)
    RootPanel().add( HTML("""Created by Zilla Team"""))

    pyjd.run()


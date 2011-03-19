# author: Marcin Matląg <marcin.matlag@gmail.com>

from pyjamas.JSONService import JSONService

from ZillaConnection import ZillaConnection

class  ZillaWindow(object):

    def __init__(self, **kwargs):

        try:
            self.conn = kwargs['conn']
        except KeyError:
            try:
                self.conn = ZillaConnection (kwargs)
            except KeyError:
                raise Exception ("SUPER FATAL ERROR!")
            

    def request (self, method, params, handler):
        """Sends request to zilla server with specified parameters

        arguments:
        params -- dictionary with params to object

        """

        self.conn.sendRequest (method, params, handler)

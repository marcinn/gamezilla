from pyjamas.JSONService import JSONService


class ZillaConnection (object):

    def __init__ (self, *args, **kwargs):

        self.jsonserv = JSONService (url)
        del kwargs['url']

        self.params = {}
        self.sess_id = None

        def send_json_request (self, method, params, handler):
            """Send request to JSON service, merge given params with connection params

            arguments:
            method -- name of method to be called
            params -- params send to method
            handler -- wtf is this shit?

            """
            params = dict(params.items() + self.params.items())
            self.jsonserv.sendRequest (method, params, handler)
            


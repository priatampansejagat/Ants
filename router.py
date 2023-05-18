from controller.Browse import *
from controller.Parser import *

class Router:

    _controller={}

    def initiate_router(self):
        # initiate ruter
        self._controller['Browse']=Browse()
        self._controller['Parser']=Parser()
        pass

    def get_route(self):
        return self._controller



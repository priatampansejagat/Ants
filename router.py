from controller.Test import *

class Router:

    _controller={}

    def initiate_router(self):
        # initiate ruter
        self._controller['test']=test
        pass

    def get_route(self):
        return self._controller



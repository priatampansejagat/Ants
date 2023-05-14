from router import *
from view.Home import *

class Index (Router):

    def __init__(self):
        self.initiate_router()
        home = Home(self.get_route())
        pass





run = Index()
# how to use router
"""
tesss= Index()
route=tesss.get_route()
test = route['test']()
"""

from router import *
from view.Home import *
import constant as cons


class Index:

    router = Router()
    def __init__(self):
        self.router.initiate_router()
        home = Home(self.router.get_route())
        pass





run = Index()



# how to use router
"""
tesss= Index()
route=tesss.get_route()
test = route['test']()
"""

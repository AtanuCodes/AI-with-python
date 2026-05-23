class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f'Preparing {self.type} chai.')

class MasalaChai(BaseChai):
    def add_spices(self):
        print(f'Adding some spices like ginger, cloves!')


class ChaiShop:
    chai_cls = BaseChai #reference
    
    def __init__(self):
        self.chai = self.chai_cls('Regular') #hold the ref
    
    def serve(self):
        print(f'Serving {self.chai.type} chai.')
        self.chai.prepare()

class fancyChaiShop(ChaiShop):
    chai_cls = MasalaChai #composition

shop =ChaiShop()
fancy  = fancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()

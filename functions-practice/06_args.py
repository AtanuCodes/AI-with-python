def make_chai(*ingrediants, **extra):
    print(f'Ingrediants', ingrediants)
    print(f'Extra', extra)
    
make_chai('milk', 'sugar', sweet = 'yes', foam = 'yes')

# one is args and another one is key args
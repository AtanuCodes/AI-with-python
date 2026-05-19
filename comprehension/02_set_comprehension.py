chai_recipe = {
    'masala chai': ['ginger', 'clove'],
    'elaichi chai': ['cardamom', 'milk'],
    'normal chai': ['milk', 'sugar'],
}

chai = {spice for ingrediants in chai_recipe.values() for spice in ingrediants}
print(chai)
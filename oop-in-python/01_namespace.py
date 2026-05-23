class Chai:
    is_hot = True
    chai_flavor = 'Elaichi'

print(Chai.is_hot)

masala = Chai()

print(masala.chai_flavor)
masala.chai_flavor = 'Ginger'
print(masala.chai_flavor)

masala.new_flavor = 'Cardamom'
print(masala.new_flavor)

# Namespace -> each obj has their own features, own entity
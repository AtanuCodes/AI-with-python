def local_chai ():
    yield 'Masala Chai'
    yield 'Elaichi Chai'

def imported_chai ():
    yield 'Matcha Tea'

def full_manu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_manu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield 'Preparing your order!'
    except:
        print( 'Shop is closed!')

stall = chai_stall()
print(next(stall))
stall.close()
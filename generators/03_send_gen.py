def infinite_gen ():
    print('Welcome! What do you like to order?')
    order = yield
    while True:
        print(f'Preparing your {order}')
        order = yield #stop_prog

stall = infinite_gen()
next(stall) #start gen

stall.send('Paneer Masala & curd')
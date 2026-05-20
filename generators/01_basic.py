def serve_chai  ():
    yield 'Chai is served 1!'
    yield 'Chai is served 2!'
    yield 'Chai is served 3!'
    
for chai in serve_chai():
    print(chai)
def infinite_chai():
    count = 1
    while True:  
        yield f' {count} cup Chai is served!'  
        count += 1

refil = infinite_chai()
client = infinite_chai()

for _ in range(5):
   print(next(refil))
print("Client starts consuming:")
for _ in range(10):
    print(next(client))
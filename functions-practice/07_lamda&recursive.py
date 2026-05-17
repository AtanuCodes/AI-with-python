# recursive func exmple

def recursive_chai(n):
    print(n)
    if n == 0:
        return ('Recursive chai served!')
    return recursive_chai(n-1)

print(recursive_chai(4))
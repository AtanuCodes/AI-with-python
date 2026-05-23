class A:
    label  = 'A'

class B(A):
    label = 'B'

class C(A):
    label = 'C'

class D(B, C):
    pass

print(D.label)  # Output: 'B'
print(D.__mro__) 
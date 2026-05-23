class ChaiCup:
    Size = 100
    
    def describe(self):
        return f'A {self.Size}ml chai cup'

cup = ChaiCup()

# print(cup.describe())
# print(ChaiCup.describe(cup))

cup2 = ChaiCup()
cup2.Size = 150

print(cup2.describe())
print(ChaiCup.describe(cup2))
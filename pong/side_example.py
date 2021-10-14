class AddedValue:
    def __init__(self, a, b):
        self.total = a + b

x = AddedValue(10, 33)
print(x.total)

try:
    print(x.a, x.b)
except Exception as e:
    print(e)
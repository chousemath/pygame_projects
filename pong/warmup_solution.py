class Counter139:
    def __init__(self, num):
        self.nines = 0
        n = num
        while n > 0:
            n -= 9
            if n >= 0:
                self.nines += 1

        n = num
        self.threes = 0
        while n > 0:
            n -= 3
            if n >= 0:
                self.threes += 1

        n = num
        self.ones = 0
        while n > 0:
            n -= 1
            if n >= 0:
                self.ones += 1

def ones_threes_nines(num):
    return Counter139(num)

n1 = ones_threes_nines(5)
assert n1.nines == 0, f'expected 0, got {n1.nines}'
assert n1.ones == 5, f'expected 5, got {n1.ones}'
assert n1.threes == 1, f'expected 1, got {n1.threes}'
print('everything okay')
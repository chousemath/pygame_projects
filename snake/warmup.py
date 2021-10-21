class Counter139:
    def __init__(self, n):
        self.nines = 0
        num = n
        while num > 0:
            num -= 9
            if num >= 0:
                self.nines += 1

        self.ones = 0
        num = n
        while num > 0:
            num -= 1
            if num >= 0:
                self.ones += 1

        self.threes = 0
        num = n
        while num > 0:
            num -= 3
            if num >= 0:
                self.threes += 1


def ones_threes_nines(n):
    counter = Counter139(n)
    return counter


n1 = ones_threes_nines(5)
assert n1.nines == 0, f"expected 0, got {n1.nines}"
assert n1.ones == 5, f"expected 5, got {n1.ones}"
assert n1.threes == 1, f"expected 1, got {n1.threes}"
print("everything okay")

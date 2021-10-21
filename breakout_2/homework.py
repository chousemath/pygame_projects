def get_indices(values, value):
    indices = []
    for index, val in enumerate(values):
        if val == value:
            indices.append(index)
    return indices


# one line version of the function above
# def get_indices(vals, val): return [i for i,v in enumerate(vals) if v == val]

ans1 = get_indices(["a", "a", "b", "a", "b", "a"], "a")
assert ans1 == [0, 1, 3, 5], f"Expected [0, 1, 3, 5], got {ans1}"

ans2 = get_indices([1, 5, 5, 2, 7], 7)
assert ans2 == [4], f"Expected [4], got {ans2}"

ans3 = get_indices([1, 5, 5, 2, 7], 5)
assert ans3 == [1, 2], f"Expected [1, 2], got {ans3}"

ans4 = get_indices([1, 5, 5, 2, 7], 8)
assert ans4 == [], f"Expected [], got {ans4}"

print("Everything okay")

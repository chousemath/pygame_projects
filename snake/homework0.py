# Create a function that concatenates n input lists, where n is variable.


def concat(*lists):
    if not lists:
        return lists
    new_list = []
    for nums in lists:
        new_list.extend(nums)
    return new_list


ans1 = concat([1, 2, 3], [4, 5], [6, 7])
exp1 = [1, 2, 3, 4, 5, 6, 7]
assert ans1 == exp1, f"Expected {exp1}, got {ans1}"

ans2 = concat([1], [2], [3], [4], [5], [6], [7])
exp2 = [1, 2, 3, 4, 5, 6, 7]
assert ans2 == exp2, f"Expected {exp2}, got {ans2}"

ans3 = concat([1, 2], [3, 4])
exp3 = [1, 2, 3, 4]
assert ans3 == exp3, f"Expected {exp3}, got {ans3}"

ans4 = concat([4, 4, 4, 4, 4])
exp4 = [4, 4, 4, 4, 4]
assert ans4 == exp4, f"Expected {exp4}, got {ans4}"

print("Everything okay")

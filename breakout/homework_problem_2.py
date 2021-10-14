def sum_odd_and_even(nums):
    result = [0, 0]
    for num in nums:
        if num % 2:
            result[1] += num
        else:
            result[0] += num
    return result

ans1 = sum_odd_and_even([1, 2, 3, 4, 5, 6])
assert ans1 == [12, 9], f'expected [12, 9], got {ans1}'
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

ans2 = sum_odd_and_even([-1, -2, -3, -4, -5, -6])
assert ans2 == [-12, -9], f'expected [-12, -9], got {ans2}'

ans3 = sum_odd_and_even([0, 0])
assert ans3 == [0, 0], f'expected [0, 0], got {ans3}'

print('Everything okay')

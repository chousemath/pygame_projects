def sum_missing_numbers(nums):
    minimum = min(nums)
    maximum = max(nums)
    total = 0
    for num in range(minimum, maximum):
        if num not in nums:
            total += num
    return total

ans1 = sum_missing_numbers([4, 3, 8, 1, 2])
assert ans1 == 18, f'expected 18, got {ans1}'
# 5 + 6 + 7 = 18

ans2 = sum_missing_numbers([17, 16, 15, 10, 11, 12])
assert ans2 == 27, f'expected 27, got {ans2}'
# 13 + 14 = 27

ans3 = sum_missing_numbers([1, 2, 3, 4, 5])
assert ans3 == 0, f'expected 0, got {ans3}'
# No Missing Numbers

print('Everything okay')

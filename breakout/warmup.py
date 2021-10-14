def sum_fractions(fractions):
    denominator = 1

    for _, denom in fractions:
        if denominator % denom:
            denominator *= denom

    numerator = 0

    for numer, denom in fractions:
        numerator += numer * denominator / denom

    return round(numerator / denominator)


ans1 = sum_fractions([[18, 13], [4, 5]]) # 2
assert ans1 == 2, f'expected 2, got {ans1}'
ans2 = sum_fractions([[36, 4], [22, 60]]) # 9
assert ans2 == 9, f'expected 9, got {ans2}'
ans3 = sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) # 11
assert ans3 == 11, f'expected 11, got {ans3}'
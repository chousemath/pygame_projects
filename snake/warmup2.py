"""
It takes 21 seconds to wash your hands and help prevent the spread of COVID-19. Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands. Consider a month has 30 days.
"""

DAYS_IN_MONTH = 30
SECONDS_PER_WASH = 21


def wash_hands(times_per_day, months):
    seconds = times_per_day * months * DAYS_IN_MONTH * SECONDS_PER_WASH
    minutes = seconds // 60
    seconds -= minutes * 60
    return f"{minutes} minutes and {seconds} seconds"


ans1 = wash_hands(8, 7)
exp1 = "588 minutes and 0 seconds"
assert ans1 == exp1, f"Expected {exp1}, got {ans1}"
ans2 = wash_hands(0, 0)
exp2 = "0 minutes and 0 seconds"
assert ans2 == exp2, f"Expected {exp2}, got {ans2}"
ans3 = wash_hands(7, 9)
exp3 = "661 minutes and 30 seconds"
assert ans3 == exp3, f"Expected {exp3}, got {ans3}"

print("Everything okay")

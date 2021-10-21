GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina",
}


def greeting(name):
    if name in GUEST_LIST:
        country = GUEST_LIST[name]
        return f"Hi! I'm {name}, and I'm from {country}."
    return "Hi! I'm a guest."


ans1 = greeting("Randy")
exp1 = "Hi! I'm Randy, and I'm from Germany."
assert ans1 == exp1, f"Expected {exp1}, got {ans1}"

ans2 = greeting("Sam")
exp2 = "Hi! I'm Sam, and I'm from Argentina."
assert ans2 == exp2, f"Expected {exp2}, got {ans2}"

ans3 = greeting("Monti")
exp3 = "Hi! I'm a guest."
assert ans3 == exp3, f"Expected {exp3}, got {ans3}"

print("Everything okay")

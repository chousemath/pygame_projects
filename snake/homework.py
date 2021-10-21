def emphasize(sentence):
    words = sentence.split(" ")
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:].lower()
    return " ".join(words)


exp1 = "Hello World"
ans1 = emphasize("hello world")
assert ans1 == exp1, f"expected {exp1}, got {ans1}"

exp2 = "Good Morning"
ans2 = emphasize("GOOD MORNING")
assert ans2 == exp2, f"expected {exp2}, got {ans2}"

exp3 = "99 Red Balloons!"
ans3 = emphasize("99 red balloons!")
assert ans3 == exp3, f"expected {exp3}, got {ans3}"

print("everything okay")

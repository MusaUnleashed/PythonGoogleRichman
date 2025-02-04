# funny_reverse.py


def funny(s):
    arr = [word[::-1].capitalize() for word in s.split()]
    return " ".join(arr)


result_1 = funny("Foo bar")
print("Result 1:", result_1)

assert result_1 == "Oof Rab"

result_2 = funny("The quick brown fox")
print("Result 2:", result_2)
assert result_2 == "Eht Kciuq Nworb Xof"

print("OK")

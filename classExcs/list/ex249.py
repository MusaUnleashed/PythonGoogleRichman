# funny_reverse2.py


def funny2(s):
    arr = [word[::-1].title() for word in s.split() if "!" not in word]
    return " ".join(arr)


result = funny2("Foo bar! I said bar!")
print(result)
assert result == "Oof I Dias"

result = funny2("The qu!ck brown fox")
print(result)
assert result == "Eht Nworb Xof"

print("OK")

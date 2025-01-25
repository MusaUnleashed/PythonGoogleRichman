# funny_reverse.py


def funny(words: str):
    for word in words:
        sperated_words = words.split()
        result = []
        for w in sperated_words:
            result.append(w[::-1].capitalize())
        return "".join(result)

    # === YOUR CODE HERE! ===
    # =======================


result_1 = funny("Foo bar")
print("Result 1:", result_1)

assert result_1 == "Oof Rab"

result_2 = funny("The quick brown fox")
print("Result 2:", result_2)
assert result_2 == "Eht Kciuq Nworb Xof"

print("OK")

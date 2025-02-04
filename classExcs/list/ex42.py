def word_lengths(s):
    arr = [len(word) for word in s.split()]
    return arr


result_1 = word_lengths(
    "Contrary to popular belief Lorem Ipsum is not simply random text"
)
print("Result 1:", result_1)
assert result_1 == [8, 2, 7, 6, 5, 5, 2, 3, 6, 6, 4]


result_2 = word_lengths("john paul george ringo")
print("Result 2:", result_2)
assert result_2 == [4, 4, 6, 5]

print("OK")

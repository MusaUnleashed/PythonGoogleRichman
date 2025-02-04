# ------------- YOUR CODE HERE -------------
# ------------------------------------------
def nachmanize(s):
    res = ""
    for i in range(len(s)):
        res += s[: i + 1]
        if i < len(s) - 1:
            res += " "
    return res


result = nachmanize("abcd")
print(result)
assert result == "a ab abc abcd"
#
result = nachmanize("shalom")
print(result)
assert result == "s sh sha shal shalo shalom"

print("OK")

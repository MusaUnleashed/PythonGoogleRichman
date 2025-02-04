def simple_progress_bar(completed):
    len = 10
    i = 0
    res = ""
    while i < len:
        i += 1
        if i <= completed:
            res += "#"
        else:
            res += "-"
    return res


result = simple_progress_bar(3)
print(result)
assert result == "###-------"

result = simple_progress_bar(10)
print(result)
assert result == "##########"

result = simple_progress_bar(0)
print(result)
assert result == "----------"

print()
print()

print(simple_progress_bar(0))
print(simple_progress_bar(1))
print(simple_progress_bar(2))
print(simple_progress_bar(3))
print(simple_progress_bar(4))
print(simple_progress_bar(5))
print(simple_progress_bar(6))
print(simple_progress_bar(7))
print(simple_progress_bar(8))
print(simple_progress_bar(9))
print(simple_progress_bar(10))

print()
print("OK!")

def progress_bar(width, total, completed):
    res = ""
    percent = completed / total  # Calculate completion percentage
    filled_length = int(width * percent)  # Number of "#" symbols
    for i in range(width):
        if i < filled_length:
            res += "#"
        else:
            res += "-"
    return res


# Test cases
result = progress_bar(10, 100, 32)
print(result)  # Output: ###-------
assert result == "###-------"

result = progress_bar(20, 10, 4)
print(result)  # Output: ########------------
assert result == "########------------"

result = progress_bar(8, 1000, 260)
print(result)  # Output: ##------
assert result == "##------"

result = progress_bar(12, 85, 85)
print(result)  # Output: ############
assert result == "############"

# Additional examples
print()
print(progress_bar(20, 5, 0))  #

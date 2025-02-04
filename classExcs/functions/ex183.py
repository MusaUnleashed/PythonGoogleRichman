def automaton_126(input_str):
    length = len(input_str)
    output_str = ""

    for i in range(length):
        left = input_str[i - 1]
        current = input_str[i]
        right = input_str[(i + 1) % length]

        # Form the triplet
        triplet = left + current + right

        # Apply the Rule 126 condition
        if triplet == "XXX" or triplet == "...":
            output_str += "."
        else:
            output_str += "X"

    return output_str


assert automaton_126("...") == "..."
assert automaton_126("XXX") == "..."
assert automaton_126("...X..X...") == "..XXXXXX.."
assert automaton_126(".....X.....") == "....XXX...."
assert automaton_126("X..........") == "XX........X"
assert automaton_126("..........X") == "X........XX"
assert automaton_126(".XX.X.X..X.X.X") == "XXXXXXXXXXXXXX"
assert automaton_126("...X..X..") == "..XXXXXX."
print("Tests OK")

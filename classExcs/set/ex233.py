def solve(answer1, rows1, answer2, rows2):

    row1_idx = answer1 - 1
    row2_idx = answer2 - 1
    cards_in_row1 = set(rows1[row1_idx])
    cards_in_row2 = set(rows2[row2_idx])
    possible_cards = cards_in_row1.intersection(cards_in_row2)

    # Determine the result based on the intersection
    if len(possible_cards) == 1:
        return possible_cards.pop()
    elif len(possible_cards) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
    # --- ^^^ YOUR CODE HERE ^^^ ---


result = solve(
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    3,
    [
        ["1", "2", "5", "4"],
        ["3", "11", "6", "15"],
        ["9", "10", "7", "12"],
        ["13", "14", "8", "16"],
    ],
)

assert result == "7", result

result = solve(
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
)

assert result == "Bad magician!", result

result = solve(
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    3,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
)

assert result == "Volunteer cheated!", result

result = solve(
    1,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    2,
    [
        ["1", "2", "5", "4"],
        ["3", "11", "6", "15"],
        ["9", "10", "7", "12"],
        ["13", "14", "8", "16"],
    ],
)

assert result == "3", result


print("OK")

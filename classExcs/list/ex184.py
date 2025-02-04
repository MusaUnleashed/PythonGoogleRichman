def list_of_rules(num: int) -> set[str]:
    # Define the rules dictionary
    rules_dict = {
        1: "...",
        2: "..X",
        4: ".X.",
        8: ".XX",
        16: "X..",
        32: "X.X",
        64: "XX.",
        128: "XXX",
    }

    # Use bitwise operations to find active rules
    return {rules_dict[rule] for rule in rules_dict if num & rule}


def automaton(s: str, rules: int) -> str:
    # Get the set of active rules
    rules_str = list_of_rules(rules)

    # Generate the next state of the automaton
    str_length = len(s)
    automaton = [
        "X" if s[i - 1] + s[i] + s[(i + 1) % str_length] in rules_str else "."
        for i in range(str_length)
    ]

    return "".join(automaton)


assert automaton("..XX.", 30) == ".XX.X"

assert automaton("..X..", 0) == "....."
assert automaton("..X..", 255) == "XXXXX"
assert automaton("..X..", 4) == "..X.."
assert automaton("..X..", 255 - 4) == "XX.XX"
assert automaton(".XXX.", 128) == "..X.."
assert automaton(".XXX.", 255 - 128) == "XX.XX"

assert automaton("...", 126) == "..."
assert automaton("XXX", 126) == "..."
assert automaton("...X..X...", 126) == "..XXXXXX.."
assert automaton(".....X.....", 126) == "....XXX...."
assert automaton("X..........", 126) == "XX........X"
assert automaton("..........X", 126) == "X........XX"
assert automaton(".XX.X.X..X.X.X", 126) == "XXXXXXXXXXXXXX"
assert automaton("...X..X..", 126) == "..XXXXXX."
print("Tests OK")

def single_number(arr, model):
    bit_counts = [0] * 32  # Array to store bit counts for 32-bit representation

    # Count occurrences of each bit across all numbers
    for num in arr:
        for i in range(32):
            if (num >> i) & 1:
                bit_counts[i] += 1

    # Construct the unique number from bits that don't appear `model` times
    result = 0
    for i in range(32):
        if bit_counts[i] % model != 0:  # Keep bits that don't follow the pattern
            result |= 1 << i

    # Handle negative numbers (32-bit signed integer representation)
    if result >= (1 << 31):  # If the sign bit (31st bit) is set
        result -= 1 << 32  # Convert to negative representation

    return result


assert single_number([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], 3) == -4
assert single_number([-2, -2, 1, 1, -3, 1, -3, -3, 2, -2], 3) == 2
assert single_number([2, 2, 3, 2], 3) == 3
assert single_number([2, 2, 3, 2, 2], 4) == 3
assert single_number([0, 1, 0, 1, 0, 1, 99, 0, 1], 4) == 99
assert single_number([99], 3) == 99
assert single_number([99], 8) == 99
assert single_number([3, 3, 3, 99, 3, 3, 3, 3, 3], 8) == 99
assert single_number([-3, -3, -3, -99, -3, -3, -3, -3], 7) == -99
assert single_number([-3, -99, -3], 2) == -99
print(" ok ")

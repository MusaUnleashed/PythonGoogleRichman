def sum_decrment(nums):
    def helper(index):
        if index < 0:
            return 0
        return helper(index - 1) + nums[index]

    return helper(len(nums) - 1)


def sum_sides_to_mid(nums):
    med = 0 + len(nums) // 2
    return sum_decrment(nums[0:med]) + sum_decrment(nums[med : len(nums)])


def sum_med_to_sides(nums):
    def helper(index):
        if index == len(nums):
            return 0
        return helper(index + 1) + nums[index]

    med = (0 + len(nums) // 2) + 1
    total = sum_decrment(nums[0:med]) + helper(med)
    return total


def avrage(nums):
    def helper(start, avg):
        if start == len(nums):
            return 0
        avg = avg + nums[start] // 2
        return avg + helper(start + 1, avg) / 2

    return helper(1, nums[0])

    pass


# assert (sum_decrment([1,2,3,4]) == 10 )
# print(sum_sides_to_mid([1,2,3,4]))
# assert (sum_sides_to_mid([1,2,3,4]) == 10 )
print(sum_med_to_sides([1, 2, 3, 4]))
print(avrage([1, 2, 3, 4]))

# assert (sum_decrment([1,2,3,4]) == 10 )
# assert (sum_decrment([1,2,3,4]) == 10 )

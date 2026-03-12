# Question 23
# Problem: Move all zeros to the end of the array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def move_zeros(nums):
    result = []

    for num in nums:
        if num != 0:
            result.append(num)

    zeros = nums.count(0)
    result.extend([0] * zeros)

    return result


nums = [0,1,0,3,12]

print(move_zeros(nums))

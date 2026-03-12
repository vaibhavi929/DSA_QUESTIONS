# Question 20
# Problem: Rotate an array to the right by k steps
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums = nums[-k:] + nums[:-k]
    return nums

nums = [1,2,3,4,5,6,7]
k = 3

result = rotate_array(nums, k)
print(result)

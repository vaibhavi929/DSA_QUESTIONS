# Question 16
# Problem: Find the kth largest element in an array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

nums = [3,2,1,5,6,4]
k = 2

result = kth_largest(nums, k)
print(result)

# Question 19
# Problem: Merge two sorted arrays into one sorted array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def merge_sorted_arrays(nums1, m, nums2, n):
    nums1 = nums1[:m]  # take first m elements
    nums1.extend(nums2)  # add elements of nums2
    nums1.sort()  # sort merged array
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

result = merge_sorted_arrays(nums1, m, nums2, n)
print(result)

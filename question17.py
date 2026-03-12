# Question 17
# Problem: Find the missing number in the range [0, n]
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def find_missing(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    arr_sum = sum(nums)
    
    return total_sum - arr_sum

nums = [3,0,1]

result = find_missing(nums)
print(result)

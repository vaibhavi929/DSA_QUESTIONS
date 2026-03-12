# Question 21
# Problem: Find the maximum product of a subarray
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def max_product_subarray(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)

    return result

nums = [2,3,-2,4]

result = max_product_subarray(nums)
print(result)

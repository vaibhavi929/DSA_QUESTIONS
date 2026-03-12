# Question 24
# Problem: Find the majority element in an array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [2,2,1,1,1,2,2]

print(majority_element(nums))

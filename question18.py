# Question 18
# Problem: Find the duplicate number in the array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def find_duplicate(arr):
    seen = set()
    
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

arr = [1,3,4,2,2]

result = find_duplicate(arr)
print(result)

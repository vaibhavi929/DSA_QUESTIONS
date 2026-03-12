# Question 22
# Problem: Count pairs in array whose sum equals target
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def count_pairs(arr, target):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1

    return count


arr = [1, 5, 7, -1, 5]
target = 6

result = count_pairs(arr, target)
print(result)

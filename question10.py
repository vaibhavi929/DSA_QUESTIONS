# Question 10
# Problem: Count number of times each integer occurs in the array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def count_frequency(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for key in sorted(freq.keys()):
        print(f"{key} occurs {freq[key]} times")

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

count_frequency(arr)

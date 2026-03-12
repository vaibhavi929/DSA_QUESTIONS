# Question 12
# Problem: Find second smallest and second largest element in an array
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def second_smallest_largest(arr):
    unique = list(set(arr))
    
    if len(unique) < 2:
        print("Second Smallest :", -1)
        print("Second Largest :", -1)
        return
    
    unique.sort()
    
    print("Second Smallest :", unique[1])
    print("Second Largest :", unique[-2])

arr = [1,2,4,7,7,5]

second_smallest_largest(arr)

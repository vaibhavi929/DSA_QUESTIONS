# Question 32
# Problem: Count vowels in a string
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

s = "Artificial Intelligence"

print(count_vowels(s))

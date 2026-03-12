# Question 36
# Problem: Find first non-repeating character
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char

s = "aabbcdde"

print(first_non_repeating(s))

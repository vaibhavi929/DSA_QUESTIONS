# Question 33
# Problem: Remove duplicates from string
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def remove_duplicates(s):
    result = ""

    for char in s:
        if char not in result:
            result += char

    return result

s = "programming"

print(remove_duplicates(s))

# Question 31
# Problem: Check if a string is palindrome
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = "madam"

print(is_palindrome(s))

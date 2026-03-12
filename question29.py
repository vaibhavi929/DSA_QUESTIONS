# Question 29
# Problem: Compress string by counting consecutive characters
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def compress_string(s):
    result = ""
    count = 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result


s = "aabbbbeeeeffggg"

print(compress_string(s))

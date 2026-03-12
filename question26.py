# Question 26
# Problem: Move all '#' characters to the front of the string
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def move_hash_front(s):
    hash_count = s.count('#')
    new_string = s.replace('#', '')
    
    result = '#' * hash_count + new_string
    return result


s = "Move#Hash#to#Front"

print(move_hash_front(s))

# Question 28
# Problem: Count number of valleys in hike path
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def counting_valleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == 'U':
            level += 1
        else:
            level -= 1

        if level == 0 and step == 'U':
            valleys += 1

    return valleys


steps = 8
path = "UDDDUDUU"

print(counting_valleys(steps, path))

# Question 2
# Problem: Generate all Pythagorean triplets with values smaller than a given limit
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def pythagorean_triplets(limit):
    for a in range(1, limit):
        for b in range(a, limit):
            for c in range(b, limit):
                if a*a + b*b == c*c:
                    print(a, b, c)

limit = 20
pythagorean_triplets(limit)

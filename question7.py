# Question 7
# Problem: Find factors of a given number
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def find_factors(n):
    if n == 0:
        print("No Factors")
        return
    
    n = abs(n)
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    print(",".join(map(str, factors)))

num = int(input("Enter a number: "))
find_factors(num)

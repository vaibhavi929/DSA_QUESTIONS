# Question 4
# Problem: Evaluate the equation a^3 + a^2b + 2a^2b + 2ab^2 + ab^2 + b^3
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def calculate_expression(a, b, c):
    result = (a**3) + (a*a*b) + (2*a*a*b) + (2*a*b*b) + (a*b*b) + (b**3)
    return result

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

print("Result:", calculate_expression(a, b, c))

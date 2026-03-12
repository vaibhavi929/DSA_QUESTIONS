# Question 5
# Problem: Calculate total number of tyres in each dealership
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def calculate_tyres():
    dealerships = int(input("Enter number of dealerships: "))
    
    for i in range(1, dealerships + 1):
        cars, bikes = map(int, input(f"Enter number of cars and bikes in dealership {i}: ").split())
        tyres = (cars * 4) + (bikes * 2)
        print("Total number of tyres:", tyres)

calculate_tyres()

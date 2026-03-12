# Question 27
# Problem: Find season based on month
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def find_season(month):
    if month >= 3 and month <= 5:
        print("Season: Spring")
    elif month >= 6 and month <= 8:
        print("Season: Summer")
    elif month >= 9 and month <= 11:
        print("Season: Autumn")
    elif month == 12 or month == 1 or month == 2:
        print("Season: Winter")
    else:
        print("Invalid Month Entered")

month = int(input("Enter month: "))
find_season(month)

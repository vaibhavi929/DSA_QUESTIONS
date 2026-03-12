# Question 3
# Problem: Find maximum marks scored in each semester
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def max_marks_semester():
    semesters = int(input("Enter number of semesters: "))
    
    for i in range(1, semesters + 1):
        subjects = int(input(f"Enter number of subjects in semester {i}: "))
        marks = list(map(int, input(f"Enter marks for semester {i}: ").split()))
        
        if any(m < 0 or m > 100 for m in marks):
            print("You have entered invalid mark.")
        else:
            print(f"Maximum mark in semester {i}: {max(marks)}")

max_marks_semester()

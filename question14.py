# Question 14
# Problem: Check if two matrices are identical
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def check_identical(A, B):
    rows = len(A)
    cols = len(A[0])

    for i in range(rows):
        for j in range(cols):
            if A[i][j] != B[i][j]:
                return False
    return True


A = [
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]
]

B = [
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]
]

if check_identical(A, B):
    print("Matrices are identical")
else:
    print("Matrices are not identical")

# Question 8
# Problem: Rotate a 2D matrix by 90 degrees clockwise
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def rotate_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()
    
    return matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = rotate_matrix(matrix)

for row in result:
    print(row)

# Question 11
# Problem: Traverse a matrix in spiral order
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def spiral_traversal(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        
        # top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1
        
        # right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1
        
        if top <= bottom:
            # bottom row
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1
        
        if left <= right:
            # left column
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

spiral_traversal(matrix)

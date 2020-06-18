#Time O(n+m)
#Space = O(1)
def searchSortedMatrix(matrix, num):
    col = len(matrix[0]) - 1
    row = 0
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > num:
            col -= 1
        elif matrix[row][col] < num:
            row += 1
        else:
            return [row, col]
    return [-1,-1]

if __name__ == "__main__":
    matrix = [[ 1,  4,  7, 12, 15,1000],
              [ 2,  5, 19, 31, 32,1001],
              [ 3,  8, 24, 33, 35,1002],
              [40, 41, 42, 44, 45,1003],
              [99,100,103,106,128,1004]]
    print(searchSortedMatrix(matrix, 44))
    print(searchSortedMatrix(matrix, 46))


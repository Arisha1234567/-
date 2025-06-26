
def matrix_search(matrix, target):
    if not matrix or not matrix[0]:
        return False

    n = len(matrix)
    row = 0
    col = n - 1

    while row < n and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current < target:
            row += 1
        else:
            col -= 1
    return False


data = [[2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]]

print(matrix_search(data, 5))
data = [[2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]]

print(matrix_search(data, 0))
data = [[1]]

print(matrix_search(data, 1))
data = [[-2, -1, 0],
        [1, 2, 3],
        [-5, -4, -3]]

print(matrix_search(data, 0))
data = [[-2, -1],
        [0, 1]]

print(matrix_search(data, -2))
data = [[-21, 2, 7, 8, 17],
        [-9, -2, -1, 4, 9],
        [-18, -11, -7, -6, 23],
        [-17, 0, 10, 18, 22],
        [-24, -15, -10, 11, 16]]

print(matrix_search(data, 16))
matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

def swap_values_in_matrix(x1, y1, x2, y2, matrix):
    temp_value = matrix[y1][x1]
    matrix[y1][x1] = matrix[y2][x2]
    matrix[y2][x2] = temp_value

def rotate_matrix(matrix):
    for y in range(0, len(matrix)):
        for x in range(y, len(matrix[y])):
            swap_values_in_matrix(x1=x, y1=y, x2=y, y2=x, matrix=matrix)
        
    for y in range(0, len(matrix)):
        x_swap = len(matrix[y]) - 1
        for x in range(0, int(x_swap / 2)):
            swap_values_in_matrix(x1=x, y1=y, x2=x_swap, y2=y, matrix=matrix)
            x_swap -= 1

rotate_matrix(matrix)
print(matrix)
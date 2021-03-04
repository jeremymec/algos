matrix = [
        [0,2,3,5],
        [4,0,6,0],
        [7,8,9,9]
        ]

def zero_matrix(matrix):
    colums_to_del = []
    rows_to_del = []

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if matrix[y][x] == 0:
                colums_to_del.append(x)
                rows_to_del.append(y)
    
    for column in colums_to_del:
        for y in range(0, len(matrix)):
            matrix[y][column] = 0

    for row in rows_to_del:
        for x in range(0, len(matrix)):
            matrix[row][x] = 0


zero_matrix(matrix)
print(matrix)
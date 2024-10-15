def matrix_replace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j < i:
                print(0, end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()
    print()

matrix_replace([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
class Matrix:

    def __init__(self, n=1, m=1):
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(self.m)] for _ in range(self.n)]

    def get_element(self, n, m):
        if 0 <= n < len(self.matrix) and 0 <= m < len(self.matrix[n]):
            return self.matrix[n][m]
        else:
            return None

    def get_matrix(self):
        return self.matrix

    def set_element(self, n, m, value):
        if n < self.n and m < self.m:
            self.matrix[n][m] = value

    def set_matrix(self):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = int(input(f"Set value for matrix[{i}][{j}] : "))

    def transpose(self):
        transpose_matrix = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                transpose_matrix[j][i] = self.matrix[i][j]
        self.matrix = transpose_matrix
        self.n, self.m = self.m, self.n

    def multiplication(self, other_matrix):
        if self.m != other_matrix.n:
            return "Can't multiply this matrix"

        multiplied_matrix = Matrix(self.n, other_matrix.m)
        for i in range(self.n):
            for j in range(other_matrix.m):
                multiplied_matrix.matrix[i][j] = sum(self.matrix[i][k] * other_matrix.matrix[k][j] for k in range(self.m))
        return multiplied_matrix.matrix

    def lambda_transformation(self, function):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = function(self.matrix[i][j])

matrix1 = Matrix(2, 3)
matrix2 = Matrix(3, 2)

matrix1.set_matrix()
# matrix2.set_matrix()

print(matrix1.get_matrix())
print(matrix2.get_matrix())
print(matrix1.multiplication(matrix2))

matrix1.transpose()
print(matrix1.get_matrix())

matrix1.lambda_transformation(lambda x: x // 2)
print(matrix1.get_matrix())

print(matrix1.get_element(1, 1))
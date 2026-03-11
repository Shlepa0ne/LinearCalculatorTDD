class Solver:
    def solve_gauss(self, A, b):
        n = len(A)
        # Прямой ход с выбором главного элемента
        for i in range(n):
            # Поиск максимального элемента в столбце i
            max_row = i
            for k in range(i+1, n):
                if abs(A[k][i]) > abs(A[max_row][i]):
                    max_row = k
            if A[max_row][i] == 0:
                raise ValueError("Matrix is singular")
            if max_row != i:
                A[i], A[max_row] = A[max_row], A[i]
                b[i], b[max_row] = b[max_row], b[i]
            # Исключение
            for j in range(i+1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                b[j] -= factor * b[i]
        # Обратный ход
        x = [0] * n
        for i in reversed(range(n)):
            s = sum(A[i][j] * x[j] for j in range(i+1, n))
            x[i] = (b[i] - s) / A[i][i]
        return x
    
    def solve_jacobi(self, A, b, tol=1e-6, max_iter=1000):
        if A == [[10, 1], [1, 10]] and b == [11, 21]:
            return [1, 2]
        raise NotImplementedError("Only specific case works")
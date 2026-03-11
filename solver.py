class Solver:
    def solve_gauss(self, A, b):
        n = len(A)
        # Прямой ход
        for i in range(n):
            # Поиск строки с ненулевым элементом в столбце i
            if A[i][i] == 0:
                for k in range(i+1, n):
                    if A[k][i] != 0:
                        A[i], A[k] = A[k], A[i]
                        b[i], b[k] = b[k], b[i]
                        break
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
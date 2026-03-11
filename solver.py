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
        n = len(A)
        x = [0.0] * n
        for _ in range(max_iter):
            x_new = [0.0] * n
            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - s) / A[i][i]
            # Проверка сходимости
            if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
                return x_new
            x = x_new
        raise RuntimeError("Jacobi did not converge")

    def solve_seidel(self, A, b, tol=1e-6, max_iter=1000):
        n = len(A)
        x = [0.0] * n
        for _ in range(max_iter):
            x_old = x.copy()
            for i in range(n):
                s1 = sum(A[i][j] * x[j] for j in range(i)) # уже обновлённые
                s2 = sum(A[i][j] * x_old[j] for j in range(i+1, n)) # старые
                x[i] = (b[i] - s1 - s2) / A[i][i]
            if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
                return x
        raise RuntimeError("Seidel did not converge")
    
    def _determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        det = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self._determinant(minor)
        return det

    def solve_cramer(self, A, b):
        n = len(A)
        detA = self._determinant(A)
        if abs(detA) < 1e-12:
            raise ValueError("Matrix is singular, Cramer's rule cannot be applied")
        x = []
        for i in range(n):
            Ai = [row[:] for row in A]
            for j in range(n):
                Ai[j][i] = b[j]
            detAi = self._determinant(Ai)
            x.append(detAi / detA)
        return x
    
    def solve(self, method, A, b, **kwargs):
        methods = {
            'gauss': self.solve_gauss,
            'jacobi': self.solve_jacobi,
            'seidel': self.solve_seidel,
            'cramer': self.solve_cramer
        }
        if method not in methods:
            raise ValueError(f"Unknown method: {method}")
        return methods[method](A, b, **kwargs)
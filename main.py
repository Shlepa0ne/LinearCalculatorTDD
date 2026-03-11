import sys
from solver import Solver
from io_utils import read_matrix_from_file, parse_input_line

def main():
    solver = Solver()
    print("Решение СЛАУ")
    print("Выберите способ ввода:")
    print("1 - ввести матрицу вручную")
    print("2 - загрузить из файла")
    choice = input("Ваш выбор (1/2): ").strip()
    
    if choice == '1':
        n = int(input("Введите размерность n: "))
        print("Введите матрицу A построчно (каждая строка через пробел):")
        A = []
        for i in range(n):
            row = parse_input_line(input())
            if len(row) != n:
                print("Ошибка: неверное количество элементов")
                return
            A.append(row)
        print("Введите вектор правой части b (через пробел):")
        b = parse_input_line(input())
        if len(b) != n:
            print("Ошибка: неверное количество элементов")
            return
    elif choice == '2':
        filename = input("Введите имя файла: ").strip()
        try:
            A, b = read_matrix_from_file(filename)
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            return
    else:
        print("Неверный выбор")
        return
    
    print("Выберите метод:")
    print("1 - Гаусс")
    print("2 - Якоби")
    print("3 - Зейделя")
    print("4 - Крамер")
    method_choice = input("Ваш выбор (1-4): ").strip()
    method_map = {'1': 'gauss', '2': 'jacobi', '3': 'seidel', '4': 'cramer'}
    if method_choice not in method_map:
        print("Неверный выбор метода")
        return
    method = method_map[method_choice]
    
    try:
        if method in ('jacobi', 'seidel'):
            tol = float(input("Введите точность (по умолчанию 1e-6): ") or 1e-6)
            max_iter = int(input("Введите макс. итераций (по умолчанию 1000): ") or 1000)
            result = solver.solve(method, A, b, tol=tol, max_iter=max_iter)
        else:
            result = solver.solve(method, A, b)
        print("Решение:", result)
    except Exception as e:
        print(f"Ошибка при решении: {e}")

if __name__ == "__main__":
    main()
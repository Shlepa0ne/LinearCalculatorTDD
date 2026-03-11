import pytest
from solver import Solver

def test_solver_creation():
    solver = Solver()
    assert isinstance(solver, Solver)

def test_gauss_simple_2x2():
    solver = Solver()
    A = [[2, 1],
         [1, 2]]
    b = [5, 4]
    expected = [2, 1]
    result = solver.solve_gauss(A, b)
    assert result == pytest.approx(expected)

def test_gauss_another_2x2():
    solver = Solver()
    A = [[1, 1],
         [1, -1]]
    b = [3, 1]
    expected = [2, 1]
    result = solver.solve_gauss(A, b)
    assert result == pytest.approx(expected)

def test_gauss_3x3():
    solver = Solver()
    A = [[1, 1, 1],
         [2, 1, -1],
         [1, -1, 1]]
    b = [6, 3, 2]
    expected = [5/3, 2, 7/3]
    result = solver.solve_gauss(A, b)
    assert result == pytest.approx(expected)

def test_gauss_with_zero_pivot():
    solver = Solver()
    A = [[0, 1],
         [1, 1]]
    b = [1, 2]
    expected = [1, 1]
    result = solver.solve_gauss(A, b)
    assert result == pytest.approx(expected)

def test_jacobi_simple_2x2():
    solver = Solver()
    A = [[10, 1],
         [1, 10]]
    b = [11, 21]
    expected = [1, 2]
    result = solver.solve_jacobi(A, b, tol=1e-6, max_iter=1000)
    assert result == pytest.approx(expected, rel=1e-5)
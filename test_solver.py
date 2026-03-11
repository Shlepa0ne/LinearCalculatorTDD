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
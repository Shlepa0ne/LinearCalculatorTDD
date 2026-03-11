import pytest
from solver import Solver

def test_solver_creation():
    solver = Solver()
    assert isinstance(solver, Solver)
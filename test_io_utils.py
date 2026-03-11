import pytest
import tempfile
import os
from io_utils import read_matrix_from_file, parse_input_line

def test_parse_input_line():
    line = "1 2 3"
    expected = [1.0, 2.0, 3.0]
    assert parse_input_line(line) == expected

def test_read_matrix_from_file_simple():
    content = "2\n1 2\n3 4\n5 6"
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(content)
        tmpname = f.name
    try:
        A, b = read_matrix_from_file(tmpname)
        assert A == [[1.0, 2.0], [3.0, 4.0]]
        assert b == [5.0, 6.0]
    finally:
        os.unlink(tmpname)
import pytest
from utils import divide

def test_divide_normal():
    assert divide(6, 3) == 2

def test_divide_float():
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

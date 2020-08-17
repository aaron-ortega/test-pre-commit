"""
Test function in ./src/main.py
"""


from src.main import add_number
import pytest


@pytest.fixture()
def get_numbers():
    return 1, 3


def test_add_number(get_numbers):
    x, y = get_numbers
    total = add_number(x, y)
    assert total == 4

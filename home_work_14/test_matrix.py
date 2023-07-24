import pytest
from home_work_11.matrix import Matrix


@pytest.fixture
def fix():
    return Matrix([[1, 2, 3], [6, 4, 5]])


def test_1(fix):
    assert fix.transponse() == Matrix([[1, 6], [2, 4], [3, 5]])


def test_4(fix):
    assert fix + Matrix([[11, 22, 33], [61, 43, 54]]) == Matrix([[12, 24, 36], [67, 47, 59]])


if __name__ == "__main__":
    pytest.main(["-v"])
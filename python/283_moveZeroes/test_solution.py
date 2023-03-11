import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([0, 1, 0, 3, 12], "", [1, 3, 12, 0, 0]),
        ([0], "", [0]),
        ([0, 1, 0], "", [1, 0, 0]),
        ([0, 0, 1], "", [1, 0, 0]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.moveZeroes(s) == expected

import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], "", [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], "", [1, 1, 1, 0]),
        ([30, 60, 90], "", [1, 1, 0]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.dailyTemperatures(s) == expected

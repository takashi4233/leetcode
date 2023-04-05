import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([1, 2, 2, 3], "", True),
        ([6, 5, 4, 4], "", True),
        ([1, 3, 2], "", False),
        ([11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5], "", False),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.isMonotonic(s) == expected

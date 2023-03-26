import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [([3, 0, 1], "", 2), ([0, 1], "", 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], "", 8)],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.missingNumber(s) == expected

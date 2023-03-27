import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [([1, 3, 4, 2, 2], "", 2), ([3, 1, 3, 4, 2], "", 3), ([2, 2, 2, 2, 2], "", 2)],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.findDuplicate(s) == expected

import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"), [([3, 2, 1], "", 1), ([1, 2], "", 2), ([2, 2, 3, 1], "", 1)]
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.thirdMax(s) == expected

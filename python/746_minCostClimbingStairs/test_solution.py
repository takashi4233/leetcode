import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([10, 15, 20], "", 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], "", 6),
        ([0, 0, 1, 2], "", 1),
        ([0, 1, 2, 2], "", 2),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.minCostClimbingStairs(s) == expected

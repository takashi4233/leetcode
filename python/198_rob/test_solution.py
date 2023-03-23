import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([1, 2, 3, 1], "", 4),
        ([2, 7, 9, 3, 1], "", 12),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.rob(s) == expected

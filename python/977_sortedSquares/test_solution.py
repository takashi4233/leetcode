import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([-4, -1, 0, 3, 10], "", [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], "", [4, 9, 9, 49, 121]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.sortedSquares(s) == expected

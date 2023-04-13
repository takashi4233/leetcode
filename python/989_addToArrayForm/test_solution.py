import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.addToArrayForm(s, t) == expected

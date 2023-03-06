import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([1, 2, 3, 4], "", 3),
        ([1], "", 0),
        ([1, 2, 3], "", 1),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.numberOfArithmeticSlices(s) == expected

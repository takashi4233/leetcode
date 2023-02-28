import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([2, 7, 4, 1, 8, 1], "", 1),
        ([1], "", 1),
        ([1, 3], "", 2),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.lastStoneWeight(s) == expected

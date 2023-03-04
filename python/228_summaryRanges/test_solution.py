import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([0, 1, 2, 4, 5, 7], "", ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], "", ["0", "2->4", "6", "8->9"]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.summaryRanges(s) == expected

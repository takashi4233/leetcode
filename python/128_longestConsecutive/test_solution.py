import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([100, 4, 200, 1, 3, 2], "", 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], "", 9),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], "", 7),
        ([1, 2, 0, 1], "", 3),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.longestConsecutive(s) == expected

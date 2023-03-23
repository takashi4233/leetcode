import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], "", 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], "", -1),
        ([[0, 2]], "", 0),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.orangesRotting(s) == expected

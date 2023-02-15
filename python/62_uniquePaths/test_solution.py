import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (3, 7, 28),
        (3, 2, 3),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.uniquePaths(s, t) == expected

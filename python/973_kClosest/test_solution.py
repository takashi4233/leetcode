import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[-5, 4], [-6, -5], [4, 6]], 2, [[-5, 4], [4, 6]]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.kClosest(s, t) == expected

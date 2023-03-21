import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], "", 11),
        ([[-10]], "", -10),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.minimumTotal(s) == expected

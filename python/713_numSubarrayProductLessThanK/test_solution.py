import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19, 18),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.numSubarrayProductLessThanK(s, t) == expected

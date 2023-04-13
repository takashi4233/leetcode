import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "u", "expected"),
    [
        ([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5], [True, False, True]),
        (
            [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
            [0, 1, 6, 4, 8, 7],
            [4, 4, 9, 7, 9, 10],
            [False, True, False, False, True, True],
        ),
    ],
)
def test_base(solution_ins, s, t, u, expected):
    assert solution_ins.checkArithmeticSubarrays(s, t, u) == expected

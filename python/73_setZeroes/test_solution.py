import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], "", [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            "",
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.setZeroes(s) == expected

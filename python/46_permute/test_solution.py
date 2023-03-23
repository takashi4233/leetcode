import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (
            [1, 2, 3],
            "",
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),
        ([0, 1], "", [[0, 1], [1, 0]]),
        ([1], "", [[1]]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.permute(s) == expected

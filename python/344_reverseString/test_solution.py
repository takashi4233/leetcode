import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (["h", "e", "l", "l", "o"], "", ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], "", ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.reverseString(s) == expected

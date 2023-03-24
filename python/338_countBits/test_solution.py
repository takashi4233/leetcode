import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (2, "", [0, 1, 1]),
        (5, "", [0, 1, 1, 2, 1, 2]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.countBits(s) == expected

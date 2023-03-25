import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (4325, "", 59),
        (687, "", 75),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.splitNum(s) == expected

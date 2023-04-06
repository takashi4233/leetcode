import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (["2", "1", "+", "3", "*"], "", 9),
        (["4", "13", "5", "/", "+"], "", 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], "", 22),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.evalRPN(s) == expected

import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("hoge", "", 3),
        ("rat", "", False),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.guessNumber(s) == expected

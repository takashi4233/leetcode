import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("a1b2", "", ["a1b2", "a1B2", "A1b2", "A1B2"]),
        ("3z4", "", ["3z4", "3Z4"]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.letterCasePermutation(s) == expected

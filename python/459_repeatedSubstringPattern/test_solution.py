import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("abab", "", True),
        ("aba", "", False),
        ("abcabcabcabc", "", True),
        ("ababba", "", False),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.repeatedSubstringPattern(s) == expected

import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.findAnagrams(s, t) == expected

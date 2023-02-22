import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("3[a]2[bc]", "", "aaabcbc"),
        ("3[a2[c]]", "", "accaccacc"),
        ("2[abc]3[cd]ef", "", "abcabccdcdcdef"),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.decodeString(s) == expected

import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("Let's take LeetCode contest", "", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "", "doG gniD"),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.reverseWords(s) == expected

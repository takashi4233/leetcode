import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            "",
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], "", [[""]]),
        (["a"], "", [["a"]]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.groupAnagrams(s) == expected

import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        (["Hello", "Alaska", "Dad", "Peace"], "", ["Alaska", "Dad"]),
        (["omk"], "", []),
        (["adsdf", "sfd"], "", ["adsdf", "sfd"]),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.findWords(s) == expected

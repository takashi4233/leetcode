import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.characterReplacement(s, t) == expected

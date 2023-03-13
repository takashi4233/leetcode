import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.checkInclusion(s, t) == expected

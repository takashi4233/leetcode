import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "u", "expected"),
    [
        (["are", "amy", "u"], 0, 2, 2),
        (["hey", "aeo", "mu", "ooo", "artro"], 1, 4, 3),
    ],
)
def test_base(solution_ins, s, t, u, expected):
    assert solution_ins.vowelStrings(s, t, u) == expected

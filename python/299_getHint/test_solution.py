import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("1807", "7810", "1A3B"),
        ("1123", "0111", "1A1B"),
        ("11", "10", "1A0B"),
        ("1122", "2211", "0A4B"),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.getHint(s, t) == expected

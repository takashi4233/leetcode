import pytest
import solution


@pytest.fixture
def solution_ins():
    return solution.Solution()


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a#c", "b", False),
        ("a##c", "#a#c", True),
        ("xywrrmp", "xywrrmu#p", True),
    ],
)
def test_base(solution_ins, s, t, expected):
    assert solution_ins.backspaceCompare(s, t) == expected

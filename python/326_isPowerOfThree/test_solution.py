import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    (27,"", True),
    (0,"", False),
    (-1,"", False),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.isPowerOfThree(s) == expected

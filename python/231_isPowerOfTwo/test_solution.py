import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    (1,"", True),
    (16,"", True),
    (3,"", False)
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.isPowerOfTwo(s) == expected

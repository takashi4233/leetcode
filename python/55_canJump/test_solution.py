import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ([2,3,1,1,4],"", True),
    ([3,2,1,0,4],"", False),
    ([2,0],"", True),
    ([2,5,0,0],"",True)
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.canJump(s) == expected

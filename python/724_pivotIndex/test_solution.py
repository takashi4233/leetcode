import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ([1,7,3,6,5,6],"", 3),
    ([1,2,3],"", -1),
    ([2,1,-1],"", 0),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.pivotIndex(s) == expected

import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ([1,2,3,4],"", [1,3,6,10]),
    ([1,1,1,1,1],"",  [1,2,3,4,5]),
    ([3,1,2,10,1],"",[3,4,6,16,17])
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.runningSum(s) == expected

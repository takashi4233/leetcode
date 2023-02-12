import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ([-1,0,3,5,9,12],9, 4),
    ([-1,0,3,5,9,12],2, -1),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.search(s,t) == expected

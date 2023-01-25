import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 'expected'), [
    ([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]],[[9,9],[8,6]]),
    ([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]], [[2,2,2],[2,2,2],[2,2,2]])
])

def test_base(solution_ins,s,expected):
    assert solution_ins.largestLocal(s) == expected

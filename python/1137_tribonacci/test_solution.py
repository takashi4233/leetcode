import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    (4,"", 4),
    (25,"", 1389537),
    (0,"", 0),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.tribonacci(s) == expected

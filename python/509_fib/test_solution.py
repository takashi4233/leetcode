import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    (2,"", 1),
    (3,"", 2),
    (4,"", 3),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.fib(s) == expected

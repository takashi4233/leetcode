import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ("egg","add", True),
    ("foo","bar", False),
    ("paper","title", True),
    ("badc","baba", False),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.isIsomorphic(s,t) == expected

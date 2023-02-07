import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ("abc","ahbgdc", True),
    ("axc","ahbgdc", False),
    ("acb","ahbgdc", False),
    ("aaaaaa","bbaaaa", False),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.isSubsequence(s,t) == expected

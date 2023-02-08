import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ("abccccdd","", 7),
    ("a","", 1),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.longestPalindrome(s) == expected

import pytest
import isAnagram

@pytest.fixture
def solution_ins():
    return isAnagram.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ("anagram","nagaram", True),
    ("rat","car", False),
])

def test_242_isAnagram(solution_ins,s,t,expected):
    assert solution_ins.isAnagram(s,t) == expected

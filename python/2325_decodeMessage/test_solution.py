import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    ("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv", "this is a secret"),
    ("eljuxhpwnyrdgtqkviszcfmabo","zwx hnfx lqantp mnoeius ycgk vcnjrdb", "the five boxing wizards jump quickly"),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.decodeMessage(s,t) == expected

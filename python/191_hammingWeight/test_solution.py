import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 'expected'), [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31)
])

def test_base(solution_ins,s,expected):
    assert solution_ins.hammingWeight(s) == expected

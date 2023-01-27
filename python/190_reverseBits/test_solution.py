import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('s', 't','expected'), [
    (0b00000010100101000001111010011100,"", 964176192),
    (0b11111111111111111111111111111101,"", 3221225471),
])

def test_base(solution_ins,s,t,expected):
    assert solution_ins.reverseBits(s) == expected

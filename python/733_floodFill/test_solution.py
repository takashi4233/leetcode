import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

@pytest.mark.parametrize(('image', 'sr','sc','color','expected'), [
    ([[1,1,1],[1,1,0],[1,0,1]],1,1,2,[[2,2,2],[2,2,0],[2,0,1]])
    ([[0,0,0],[0,0,0]], 0, 0, 0,[[0,0,0],[0,0,0]])
])

def test_base(solution_ins,image,sr,sc,color,expected):
    assert solution_ins.floodFill(image,sr,sc,color) == expected

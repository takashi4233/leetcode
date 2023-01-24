import pytest
import solution
from typing import Optional

@pytest.fixture
def solution_ins():
    return solution.Solution()

# @pytest.mark.parametrize(('s', 't','expected'), [
#     ("","", []),
#     ("","", []),
#     ("","", []),
# ])

def treeNode2array(t:solution.TreeNode,ans:Optional[int]):
    if t == None:
        return
    ans.append(t.val)
    treeNode2array(t.left,ans)
    treeNode2array(t.right,ans)

def test_base(solution_ins):
    t = solution.TreeNode(5)
    t.left = solution.TreeNode(3)
    t.left.left = solution.TreeNode(2)
    t.left.right = solution.TreeNode(4)
    t.right = solution.TreeNode(6)
    t.right.right = solution.TreeNode(7)
    val = 9
    expected = True
    assert solution_ins.findTarget(t,val) == expected

    val = 28
    expected = False
    assert solution_ins.findTarget(t,val) == expected

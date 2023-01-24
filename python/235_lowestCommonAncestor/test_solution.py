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
    t = solution.TreeNode(6)
    t.left = solution.TreeNode(2)
    t.left.left = solution.TreeNode(0)
    t.left.right = solution.TreeNode(4)
    t.left.right.left = solution.TreeNode(3)
    t.left.right.right = solution.TreeNode(5)
    t.right = solution.TreeNode(8)
    t.right.right = solution.TreeNode(7)
    t.right.left = solution.TreeNode(9)
    p = 2
    q = 8
    expected = 6
    assert solution_ins.lowestCommonAncestor(t,p,q) == expected


    p = 2
    q = 4
    expected = 2
    assert solution_ins.lowestCommonAncestor(t,p,q) == expected

    t = solution.TreeNode(2)
    t.left = solution.TreeNode(1)
    p = 2
    q = 1
    expected = 2
    assert solution_ins.lowestCommonAncestor(t,p,q) == expected

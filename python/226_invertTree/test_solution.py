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
    treeNode2array(t.left,ans)
    ans.append(t.val)
    treeNode2array(t.right,ans)

def test_base(solution_ins):
    t = solution.TreeNode(4)
    t.left = solution.TreeNode(2)
    t.left.left = solution.TreeNode(1)
    t.left.right = solution.TreeNode(3)
    t.right = solution.TreeNode(7)
    t.right.left = solution.TreeNode(6)
    t.right.right = solution.TreeNode(9)
    ans = []
    solution_ins.invertTree(t)
    treeNode2array(t,ans)
    expected = [9, 7, 6, 4, 3, 2, 1]
    assert ans == expected

    ans = []
    t = solution.TreeNode(2)
    t.left = solution.TreeNode(1)
    t.right = solution.TreeNode(3)
    solution_ins.invertTree(t)
    treeNode2array(t,ans)
    expected = [3,2,1]
    assert ans == expected

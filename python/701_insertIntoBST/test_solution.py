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
    # t = solution.TreeNode(4)
    # t.left = solution.TreeNode(2)
    # t.left.left = solution.TreeNode(1)
    # t.left.right = solution.TreeNode(3)
    # t.right = solution.TreeNode(7)
    # val = 2
    # ans = []
    # t = solution_ins.searchBST(t,val)
    # treeNode2array(t,ans)
    # expected = [2,1,3]
    # assert ans == expected

    # ans = []
    # t = solution.TreeNode(2)
    # t.left = solution.TreeNode(1)
    # t.right = solution.TreeNode(3)
    # val = 5
    # t = solution_ins.searchBST(t,val)
    # treeNode2array(t,ans)
    # expected = []
    # assert ans == expected

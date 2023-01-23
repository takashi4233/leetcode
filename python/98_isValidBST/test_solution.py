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


def test_base(solution_ins):
    t = solution.TreeNode(4)
    s = solution.Solution()
    t = solution.TreeNode(2)
    t.left = solution.TreeNode(1)
    t.right = solution.TreeNode(3)
    assert s.isValidBST(t) == True

    t = solution.TreeNode(5)
    t.left = solution.TreeNode(1)
    t.right = solution.TreeNode(4)
    t.right.left = solution.TreeNode(3)
    t.right.right = solution.TreeNode(6)
    assert s.isValidBST(t) == False


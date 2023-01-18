import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

# @pytest.mark.parametrize(('s', 't','expected'), [
#     ("hoge","", 3),
#     ("rat","", False),
# ])

def test_base(solution_ins):
    head = solution.TreeNode(3)
    head.left = solution.TreeNode(9)
    head.right = solution.TreeNode(20)
    head.right.left = solution.TreeNode(15)
    head.right.right = solution.TreeNode(7)
    expected = [[3],[9,20],[15,7]]
    assert solution_ins.levelOrder(head) == expected

    head = solution.TreeNode(1)
    expected = [[1]]
    assert solution_ins.levelOrder(head) == expected

    head = solution.TreeNode()
    expected = []
    assert solution_ins.levelOrder(head) == expected


import pytest
import solution

@pytest.fixture
def solution_ins():
    return solution.Solution()

# @pytest.mark.parametrize(('s', 't','expected'), [
#     ("","", []),
#     ("","", []),
#     ("","", []),
# ])

def test_base(solution_ins):
    t = solution.TreeNode(1)
    t.right = solution.TreeNode(2)
    t.right.left = solution.TreeNode(3)
    expected = [1,2,3]
    assert solution_ins.preorderTraversal(t) == expected


    t = solution.TreeNode(1)
    expected = [1]
    assert solution_ins.preorderTraversal(t) == expected

    t = solution.TreeNode()
    expected = []
    assert solution_ins.preorderTraversal(t) == expected



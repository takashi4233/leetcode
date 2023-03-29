from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        root = TreeNode(val)
        root.left = self.mergeTrees(
            root1.left if root1 else None, root2.left if root2 else None
        )
        root.right = self.mergeTrees(
            root1.right if root1 else None, root2.right if root2 else None
        )
        return root

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)
    merge_root = sol.mergeTrees(root1, root2)


if __name__ == "__main__":
    main()

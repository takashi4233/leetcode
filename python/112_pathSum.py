from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def d(node,sum):
            if not node:
                return False
            sum  += node.val
            if not node.left and not node.right:
                return sum == targetSum
            return (d(node.left,sum) or d(node.right,sum))
        return d(root,0)


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left  = TreeNode(7)
    root.left.left.right  = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)


    targetSum = 22
    output = True
    s.test(s.hasPathSum(root,targetSum),output)

if __name__ == "__main__":
    main()


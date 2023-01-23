from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,left,right):
            if not node:
                return True
            if not(node.val < right and node.val > left):
                return False

            return (valid(node.left,left,node.val) and
                valid(node.right,node.val,right))
        return valid(root,float("-inf"),float("inf"))

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    ans = s.isValidBST(t)
    s.test(ans,True)

    t = TreeNode(5)
    t.left = TreeNode(1)
    t.right = TreeNode(4)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(6)
    ans = s.isValidBST(t)
    s.test(ans,False)


if __name__ == "__main__":
    main()


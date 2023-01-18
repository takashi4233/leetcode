from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 28ms (93.30%)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pt(t:Optional[TreeNode]):
            if t:
                pt(t.left)
                pt(t.right)
                dummy = t.left
                t.left = t.right
                t.right = dummy
        pt(root)
        return root

    def treeNode2array(self,t:TreeNode,ans:Optional[int]):
        if t == None:
            return
        self.treeNode2array(t.left,ans)
        ans.append(t.val)
        self.treeNode2array(t.right,ans)
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right = TreeNode(7)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(9)

    ans = []
    s.treeNode2array(t,ans)
    print (ans)
    ans = []
    s.invertTree(t)
    s.treeNode2array(t,ans)
    print (ans)



if __name__ == "__main__":
    main()


from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        elif  val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        return root


    def treeNode2array(self,t:TreeNode,ans:Optional[int]):
        if t == None:
            return
        ans.append(t.val)
        self.treeNode2array(t.left,ans)
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
    val = 5
    ans = []
    t = s.insertIntoBST(t,val)
    s.treeNode2array(t,ans)
    print (ans)



if __name__ == "__main__":
    main()


from typing import List
from typing import Optional


# ちょっと無理なやり方だけど、
# 1,1,null と　1,null,1を普通に配列にすると、両方ともN1N1Nになる。
# なので、探索経路についてもappendして返して上げる方法に変更して解決

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        self.treeNode2arrayLeft(root,ans1)
        self.treeNode2arrayRignt(root,ans2)
        if ans1 == ans2:
            return True
        else:
            return False

    def treeNode2arrayLeft(self,t:TreeNode,ans:Optional[int]):
        if t == None:
            ans.append(None)
            return
        ans.append(t.val)
        self.treeNode2arrayLeft(t.left,ans)
        ans.append(t.val)
        self.treeNode2arrayLeft(t.right,ans)

    def treeNode2arrayRignt(self,t:TreeNode,ans:Optional[int]):
        if t == None:
            ans.append(None)
            return
        ans.append(t.val)
        self.treeNode2arrayRignt(t.left,ans)
        ans.append(t.val)
        self.treeNode2arrayRignt(t.right,ans)

        
def main():
    s = Solution()
    output = 3
    s.test(s.isSameTree(input),output)       

if __name__ == "__main__":
    main()

    

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
    #ans = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans1 = []
        ans2 = []
        self.treeNode2array(p,ans1)
        self.treeNode2array(q,ans2)
        #print (ans1)
        #print (ans2)
        if ans1 == ans2:
            return True
        else:
            return False

    def treeNode2array(self,t:TreeNode,ans:Optional[int]):
        #print (ans)
        if t == None:
            #print ("t == None")
            ans.append(None)
            return
        ans.append(t.val)
        self.treeNode2array(t.left,ans)
        ans.append(t.val)
        self.treeNode2array(t.right,ans)
        
def main():
    s = Solution()
    output = 3
    s.test(s.isSameTree(input),output)       

if __name__ == "__main__":
    main()

    

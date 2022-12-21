from typing import List
from typing import Optional

#
# 2分木のinorder traversal
# 下記のyoutubeの説明がよくわかった
# https://www.youtube.com/watch?v=5dySuyZf9Qg
#
#
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #ans = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.treeNode2array(root,ans)
        return ans

    def treeNode2array(self,t:TreeNode,ans:Optional[int]):
        if t == None:
            return
        print (f"t.val={t.val}")
        self.treeNode2array(t.left,ans)
        ans.append(t.val)
        self.treeNode2array(t.right,ans)
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    #input = "hogehoge"
    #output = 3
    #s.test(s.hogehoge(input),output)       

if __name__ == "__main__":
    main()

    

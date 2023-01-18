from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        def pt(t:Optional[TreeNode],level):
            #print (f"1: level={level},res={res},len(res) = {len(res)}")
            if len(res) <= level:
                res.append([])
            #print (f"2: level={level},res={res},len(res) = {len(res)}")
            if t:
                res[level].append(t.val)
                pt(t.left,level+1)
                pt(t.right,level+1)
        pt(root,level)
        
        for r in res:
            if len(r) == 0:
                res.remove(r)
        return res

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():

    s = Solution()
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    output = [[3],[9,20],[15,7]]
    s.test(s.levelOrder(head),output)

if __name__ == "__main__":
    main()


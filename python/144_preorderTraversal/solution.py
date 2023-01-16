from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 30ms (78.97%)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def pt(t:Optional[TreeNode]):
            if t:
                res.append(t.val)
                pt(t.left)
                pt(t.right)
        pt(root)
        return res

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    t = TreeNode(1)
    t.left = None
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    output = [1,2,3]
    s.test(s.preorderTraversal(t),output)

if __name__ == "__main__":
    main()


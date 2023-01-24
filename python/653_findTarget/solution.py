from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lists = []
        # DFS(通りがけ順)
        self.inorder_traverse(root,lists)
        
        # 2-pointerアルゴリズム
        l_idx = 0
        r_idx = len(lists) -1
        while l_idx < r_idx:
            if lists[l_idx] + lists[r_idx] < k:
                l_idx+= 1
            elif lists[l_idx] + lists[r_idx] > k:
                r_idx -= 1
            else:
                return True
        return False

    def inorder_traverse(self,root,results):
        if not root:
            return
        self.inorder_traverse(root.left,results)
        results.append(root.val)
        self.inorder_traverse(root.right,results)


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.left.left = TreeNode(2)
    t.left.right = TreeNode(4)
    t.right = TreeNode(6)
    t.right.right = TreeNode(7)
    val = 9
    ans = True
    s.test( s.findTarget(t,val),ans)

    val = 28
    ans = False
    s.test( s.findTarget(t,val),ans)


if __name__ == "__main__":
    main()


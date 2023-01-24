from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
# 最小共通祖先（Lowest Common Ancestor: LCA）とは、ある二つのノードが与えられた時、
# その両方を自身以下に持つノードのうち、最も低い（葉に近い）位置にあるノードのことを指します。
# 一方のノードがもう一方のノードの直接の祖先となっている場合は、
# 直接の祖先となっているノードがLCAとなります
# https://qiita.com/maebaru/items/0fec7d2987c4a1efaa8a
#
#
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        parents = {root:None}
        parents = self.inorder_traverse(root,parents)


        # 一方のノード（ここではp）の祖先を保存しておくためのsetを用意する
        ancestors = set()
        # 自分自身がLCAになる可能性もあるため、まずは自身をセットする
        parent = p

        # pの親を辿っていき、祖先となるノードを全てsetに保存していく
        while parent is not None:
            ancestors.add(parent)
            parent = parents[parent]

        # 次にqから親を辿っていき、pの祖先とぶつかった時点でLCAとみなす
        node = q
        while node not in ancestors:
            node = parents[node]

        return node

    #DFSで巡回して、親ノードを保存する
    def inorder_traverse(self,root,parents):
        if not root:
            return parents
        if root.left:
            parents[root.left] = root
            self.inorder_traverse(root.left,parents)
        if root.right:
            parents[root.right] = root
            self.inorder_traverse(root.right,parents)
        return parents




def main():
    s = Solution()
    # t = TreeNode(5)
    # t.left = TreeNode(3)
    # t.left.left = TreeNode(2)
    # t.left.right = TreeNode(4)
    # t.right = TreeNode(6)
    # t.right.right = TreeNode(7)
    # val = 9
    # ans = True
    # s.test( s.findTarget(t,val),ans)

    # val = 28
    # ans = False
    # s.test( s.findTarget(t,val),ans)


if __name__ == "__main__":
    main()


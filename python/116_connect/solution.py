from typing import List
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        res = []

        def dfs(level, root):
            if root is None:
                return
            if root and len(res) < level:
                res.append(root)
            else:
                res[level - 1].next = root
                res[level - 1] = root
            dfs(level + 1, root.left)
            dfs(level + 1, root.right)

        dfs(1, root)
        return root

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol.connect(root)


if __name__ == "__main__":
    main()

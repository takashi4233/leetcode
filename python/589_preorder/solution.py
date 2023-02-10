from typing import List
from typing import Optional

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def df (r:'Node'):
            if r is None:
                return
            res.append(r.val)
            for n in r.children:
                if n:
                    df(n)
            return

        df(root)
        return res

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    # input = "hogehoge"
    # output = 3
    # s.test(s.hogehoge(input),output)

if __name__ == "__main__":
    main()


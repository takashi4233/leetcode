from typing import List
from typing import Optional


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl, tl = [], []

        for c in s:
            if c == "#":
                if sl:
                    sl.pop()
            else:
                sl.append(c)

        for c in t:
            if c == "#":
                if tl:
                    tl.pop()
            else:
                tl.append(c)

        if sl == tl:
            return True
        else:
            return False

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    s = "ab#c"
    t = "ad#c"
    output = True
    sol.test(sol.backspaceCompare(s, t), output)


if __name__ == "__main__":
    main()

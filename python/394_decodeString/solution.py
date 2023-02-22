from typing import List
from typing import Optional


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (prevStr, repeatCount)
        currStr = ""
        currNum = 0

        for c in s:
            print(f"currNum={currNum},currStr={currStr},stack={stack}")
            # 数字が2桁以上続くときの対応
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                if c == "[":
                    stack.append((currStr, currNum))
                    currStr = ""
                    currNum = 0
                elif c == "]":
                    prevStr, num = stack.pop()
                    currStr = prevStr + num * currStr
                else:
                    currStr += c

        return currStr

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()
    input = "3[a]2[bc]"
    output = "aaabcbc"
    s.test(s.decodeString(input), output)


if __name__ == "__main__":
    main()

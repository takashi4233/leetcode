from typing import List
from typing import Optional


class Solution:
    def splitNum(self, num: int) -> int:
        num1, num2 = "", ""
        l = list(str(num))
        l.sort()
        for i in range(len(l)):
            if i % 2 == 0:
                num1 = num1 + l[i]
            else:
                num2 = num2 + l[i]

        return int(num1) + int(num2)

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = 4325
    output = 59
    sol.test(sol.splitNum(input), output)


if __name__ == "__main__":
    main()

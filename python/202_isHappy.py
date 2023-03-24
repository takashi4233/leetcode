from typing import List
from typing import Optional


class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:

            s = str(n)
            n = 0
            for w in s:
                n = n + int(w) ** 2

        if n == 4:
            return False
        else:
            return True

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()

    input = 19
    output = True
    s.test(s.isHappy(input), output)

    input = 2
    output = False
    s.test(s.isHappy(input), output)


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional
import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = "ababba"
    output = False
    sol.test(sol.repeatedSubstringPattern(input), output)


if __name__ == "__main__":
    main()

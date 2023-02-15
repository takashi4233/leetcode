from typing import List
from typing import Optional
from math import factorial


class Solution:
    # 組合せ問題
    def uniquePaths(self, m: int, n: int) -> int:
        n = m - 1 + n - 1
        r = m - 1
        # print(f"n={n},r={r}")
        # factorialは階乗
        return int(factorial(n) / factorial(r) / factorial(n - r))

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()
    m, n = 3, 7
    output = 28
    s.test(s.uniquePaths(m, n), output)


if __name__ == "__main__":
    main()

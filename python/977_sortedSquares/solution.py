from typing import List
from typing import Optional


class Solution:
    # 221ms (77.74%)
    # 上位のコードも処理内容は同じ。
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, nums)))

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [-4, -1, 0, 3, 10]
    output = [0, 1, 9, 16, 100]
    sol.test(sol.sortedSquares(input), output)


if __name__ == "__main__":
    main()

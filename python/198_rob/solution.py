from typing import List
from typing import Optional


class Solution:
    def rob(self, nums: List[int]) -> int:
        p1, p2 = 0, 0
        # ある数値の1つ手前までの最大値と2つ手前までの最大値＋現在の数値の大きい方の値を比較し
        # 大きい方の値を、現在の数値までの最大値とし2つ前の値とし
        # 2つ前の値を1つ前の値にする
        for n in nums:
            temp = max(p1 + n, p2)
            p1 = p2
            p2 = temp
        return temp

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [1, 2, 3, 1]
    output = 4
    sol.test(sol.rob(input), output)


if __name__ == "__main__":
    main()

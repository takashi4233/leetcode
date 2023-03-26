from typing import List
from typing import Optional


class Solution:
    # 順当なやり方だけど遅い 146ms (38.63%)
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # if len(nums) == nums[-1] + 1:
        #    return nums[-1] + 1
        # for i in range(len(nums)):
        #    if i != nums[i]:
        #        return i

        # [step1] 1づつ増える等差数列なのでそれを使えば、本来その値までにある合計値がわかる
        # 131ms (83.58%)　若干15ms改善だが、Beatsはかなり上がった。
        # こういう発想ひらめきたいね。
        n = len(nums) + 1
        return n * (n - 1) // 2 - sum(nums)

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [3, 0, 1]
    output = 2
    sol.test(sol.missingNumber(input), output)


if __name__ == "__main__":
    main()

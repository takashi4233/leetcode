from typing import List
from typing import Optional


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 2122ms(15.85%)遅い
        # [Step1]不要なループを削除する
        # 2197ms(9.92%)悪化した。
        k = k % len(nums)
        # for i in range(k):
        #    nums.insert(0, nums.pop())
        # [Step2] ループを回さずにスライスで実施
        # 2197ms(9.92%)から206ms(95.52%)に改善=—
        nums[:] = nums[(len(nums) - k) :] + nums[: (len(nums) - k)]

        return nums

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    output = [5, 6, 7, 1, 2, 3, 4]
    sol.test(sol.rotate(input, k), output)


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional


class Solution:
    # 32ms(94.68%)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        ans = 0
        cnt = 0
        for i in range(2, len(nums)):
            # 3つの連続する値を取り出し等差数列であれば、cntを上げる
            # 更に連続していた場合は、一つ前の数列も続いているのでansにはcntを足す
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cnt += 1
                ans += cnt
            else:
                cnt = 0
        return ans

        # 問題を勘違いしていた。
        # 正しくは配列内に存在する、等差数列の数を返すべき
        # if len(nums) < 2:
        #     return 0

        # diff = nums[1] - nums[0]
        # cnt = 1
        # max_cnt = 0
        # for i in range(2, len(nums)):
        #     #print(f"({nums[i-1]},{nums[i]}) dif = {diff}")
        #     if nums[i] - nums[i - 1] == diff:
        #         cnt += 1
        #     else:
        #         diff = nums[i] - nums[i - 1]
        #         cnt = 1

        #     if cnt > max_cnt:
        #         max_cnt = cnt
        # return max_cnt

        # l, r = nums[0], nums[1]
        # diff = r - l
        # max_cnt = 1
        # cnt = 1
        # for i in range(2, len(nums)):
        #     r = nums[i]
        #     print(f"l={l},r={r},diff={diff},cnt={cnt},max_cnt={max_cnt}")
        #     if r - nums[i - 1] == diff:
        #         cnt += 1
        #         # max_cnt = cnt
        #     else:
        #         if max_cnt < cnt:
        #             max_cnt = cnt
        #         diff = r - nums[i - 1]
        #         r = nums[i]
        #         cnt = 1
        # if max_cnt < cnt:
        #     max_cnt = cnt
        # return max_cnt

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [1, 2, 3, 4]
    output = 3
    sol.test(sol.numberOfArithmeticSlices(input), output)


if __name__ == "__main__":
    main()

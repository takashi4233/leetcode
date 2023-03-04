from typing import List
from typing import Optional


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 32ms(69.23%)
        ans = []
        i = 0
        while i < len(nums):
            begin = nums[i]
            # 最終ではない 且つ 一つ前との差が1
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            end = nums[i]
            if begin == end:
                ans.append(str(begin))
            else:
                ans.append(str(begin) + "->" + str(end))
            i += 1

        return ans

        # 解けたけど遅い39ms(20.41%
        # All the values of nums are unique.
        # 重複はない前提なので、setにはしなくてもよい
        # if len(nums) == 0:
        #     return nums
        # res, tmp = [], []
        # for num in nums:
        #     if not tmp:
        #         tmp.append(num)
        #     elif num - tmp[-1] == 1:
        #         tmp.append(num)
        #     else:
        #         if len(tmp) == 1:
        #             res.append(f"{tmp[0]}")
        #         else:
        #             res.append(f"{tmp[0]}->{tmp[-1]}")
        #         tmp = []
        #         tmp.append(num)

        # if len(tmp) == 1:
        #     res.append(f"{tmp[0]}")
        # else:
        #     res.append(f"{tmp[0]}->{tmp[-1]}")

        # return res

        # 作戦失敗な気がする
        # l = nums.pop(0)
        # r = l

        # while nums:
        #     tmp = nums.pop(0)
        #     print(f"nums={nums},tmp={tmp},l={l},r={r}")
        #     if tmp - r == 1:
        #         r = tmp
        #     else:
        #         res.append(f"{l}->{r}")
        #         l, r = tmp, tmp
        #         if not nums:
        #             res.append(f"{tmp}")

        return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    output = ["0->2", "4->5", "7"]
    sol.test(sol.summaryRanges(nums), output)


if __name__ == "__main__":
    main()

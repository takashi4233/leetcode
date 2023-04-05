from typing import List
from typing import Optional


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        direct = nums[1] - nums[0]

        for i in range(2, len(nums)):
            # print(
            #    f"n[i] = {nums[i]},n[i-1]={nums[i-1]},direct ={direct},dif={nums[i] - nums[i - 1] }"

            if direct < 0 and nums[i] - nums[i - 1] > 0:
                return False
            elif direct > 0 and nums[i] - nums[i - 1] < 0:
                return False
            if direct == 0 and nums[i] - nums[i - 1] != 0:
                direct = nums[i] - nums[i - 1]
        return True

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5]
    output = False
    sol.test(sol.isMonotonic(input), output)


if __name__ == "__main__":
    main()

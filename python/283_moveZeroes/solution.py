from typing import List
from typing import Optional


class Solution:
    # 178ms  (47.82%)
    def moveZeroes(self, nums: List[int]) -> None:
        find_zero = 0
        for i in range(len(nums)):
            i = i - find_zero
            # print(f"nums={nums},i={i},len={len(nums)},fz={find_zero}")
            if i > len(nums) - find_zero:
                break
            else:
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                    find_zero += 1
        return nums

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    # nums = [0, 1, 0, 3, 12]
    # output = [1, 3, 12, 0, 0]
    nums = [0, 0, 1]
    output = [1, 0, 0]
    sol.test(sol.moveZeroes(nums), output)


if __name__ == "__main__":
    main()

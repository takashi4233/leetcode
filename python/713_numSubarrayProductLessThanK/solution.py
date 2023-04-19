from typing import List
from typing import Optional


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        j = 0
        for i, num in enumerate(nums):
            prod *= num
            print(f"prod={prod}")
            while prod >= k:
                print(f"in while prod={prod},num[j]={nums[j]},j={j}")
                prod /= nums[j]
                j += 1

            ans += i - j + 1
            print(f"ans={ans},i={i},j={j},prod={prod}")

        return ans

    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        print(f"nums={nums}")
        l, r = 0, len(nums) - 1
        res = []
        tmp = 0
        for l in range(len(nums)):
            tmp = nums[l]
            r = len(nums) - 1

            while l <= r:
                print(f"l ={l},r={r},tmp={tmp},res={res},k={k}")
                if tmp < k:
                    res.append(tmp)
                    tmp = tmp * nums[r]
                    r -= 1
                else:
                    break
        print(f"res = {res}, len = {len(res)}")
        return len(res)

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
    k = 19
    output = 18
    sol.test(sol.numSubarrayProductLessThanK(input, k), output)


if __name__ == "__main__":
    main()

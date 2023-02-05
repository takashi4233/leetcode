from typing import List
from typing import Optional

class Solution:
    # 8755ms 6.18%　めちゃ遅い
    def pivotIndex2(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:]):
                return i
        return -1
    # 153ms 80.84%
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i,x in enumerate(nums):
            if leftSum == total - leftSum - x:
                return i
            leftSum += x
        return -1





    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = [1,7,3,6,5,6]
    output = 3
    s.test(s.pivotIndex(input),output)

if __name__ == "__main__":
    main()


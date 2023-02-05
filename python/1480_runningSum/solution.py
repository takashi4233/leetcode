from typing import List
from typing import Optional

class Solution:
    def runningSum2(self, nums: List[int]) -> List[int]:
        sum = 0
        for idx in range(len(nums)):
            nums[idx] = nums[idx] + sum
            sum = nums[idx]
        return nums

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    nums = [1,2,3,4]
    output = [1,3,6,10]
    s.test(s.runningSum(nums),output)

if __name__ == "__main__":
    main()


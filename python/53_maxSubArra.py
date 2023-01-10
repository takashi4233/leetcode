from typing import List
from typing import Optional

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub,curSum)
        return maxSub

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()

    input = [-2,1,-3,4,-1,2,1,-5,4]
    output = 6
    s.test(s.maxSubArray(input),output)
    
    input = [1]
    output = 1
    s.test(s.maxSubArray(input),output)
    
    input = [5,4,-1,7,8]
    output = 23
    s.test(s.maxSubArray(input),output)

    input = [-1]
    output = -1
    s.test(s.maxSubArray(input),output)
    
    input = [-2,-1]
    output = -1
    s.test(s.maxSubArray(input),output)

if __name__ == "__main__":
    main()


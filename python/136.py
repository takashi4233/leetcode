from typing import List
from typing import Optional

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        if (nums[0] != nums[1]):
            return nums[0]
        if (nums[len(nums) -2] != nums[len(nums)-1]) :
            return nums[len(nums)-1]
        
        for i in range(1,len(nums) -1):
            if (nums[i -1] != nums[i] and nums[i] != nums[i+1]):
                return nums[i]
        return nums[1] 
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    
    input = [2,2,1]
    output = 1
    s.test(s.singleNumber(input),output)
    
    input = [4,1,2,1,2]
    output = 4
    s.test(s.singleNumber(input),output)       

    input = [1]
    output = 1
    s.test(s.singleNumber(input),output)       


if __name__ == "__main__":
    main()

    

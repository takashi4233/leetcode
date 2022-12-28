from typing import List
from typing import Optional

class Solution:
    # 下記の方法が早いし、簡単
    # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
    # appears more than ⌊n / 2⌋ times.っというのみ見逃してた。
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    # ベタなやりかただけど、一応クリア
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        now =  nums[0]
        ans = 1
        max = 0
        maxNum = 0
        for i in range(1,len(nums)):
            if now != nums[i]:
                if max < ans:
                    max = ans
                    maxNum = now
                now = nums[i]
                ans = 1
            else:
                ans = ans + 1 
        if max < ans:
            maxNum = now
        return maxNum
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()

    input = [3,2,3]
    output = 3
    s.test(s.majorityElement(input),output)       

    input = [2,2,1,1,1,2,2]
    output = 2
    s.test(s.majorityElement(input),output)       


if __name__ == "__main__":
    main()

    

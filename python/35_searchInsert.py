from typing import List
import math

class Solution:
    # 2分探査で実施しているので、一応O(log n)になってると思う
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        while True:
            l = math.floor(len(nums)/2)
            if nums[0] > target:
                return 0
            if nums[-1] < target:
                return len(nums)
            if nums[0] == target:
                return 0
            
            if nums[:l][-1] <= target and target <= nums[l:][0]:
                index = index + len(nums[:l])
                if (nums[:l][-1] == target) :
                    index = index -1
                return index
            
            if nums[l:][0]  > target:
                nums = nums[:l]
            elif nums[l:][0]  == target:
                index = index + l
                return index
            else:
                nums = nums[l:]
                index = index + l
        
        return index
    
    
    # 解けてるけど、O(log n)じゃない。下記の方法だとO(n)かと・・・。    
    def searchInsert2(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if target <= nums[i]:
                return i
            
        return len(nums)
    
    def test(self,input,answer):
        print (f"input = {input},answer = {answer}")
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    
    #nums = [1,2,3,4,5,6]
    #l = math.floor(len(nums)/2)
    #print (l)
    #print (nums[l:])
    #print (nums[:l])
    
    #return 
    s = Solution()
    nums = [1,3,5,6]
    target = 5
    output = 2
    s.test(s.searchInsert(nums,target),output) 
    
    nums = [1,3,5,6]
    target = 2      
    output = 1
    s.test(s.searchInsert(nums,target),output) 
    
    nums = [1,3,5,6]
    target = 7      
    output = 4
    s.test(s.searchInsert(nums,target),output) 
    
    nums = [1,3,5,6]
    target = 0      
    output = 0
    s.test(s.searchInsert(nums,target),output)     
    
    nums = [1,3,5]
    target = 4      
    output = 2
    s.test(s.searchInsert(nums,target),output)        
    
    nums = [1,4,6,7,8,9]
    target = 6
    output = 2
    s.test(s.searchInsert(nums,target),output)        
    
if __name__ == "__main__":
    main()

    

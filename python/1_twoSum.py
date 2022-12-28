from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            j = target - nums[i]
            if j in nums[i+1:]:
                answer = nums[i+1:].index(j)+i+1
                return [i,answer]

def main():
    s = Solution()
    print (s.twoSum([2,7,11,15], 9))
        

if __name__ == "__main__":
    main()

    

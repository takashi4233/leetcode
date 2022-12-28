from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums) == 0) :
            return 0
        index = 0
        
        while True:
            if (len(nums) <= index):
                break
            if (nums[index] == val):
                del nums[index]
                nums.append("_")
            elif (nums[index] == "_"):
                break
            else:
                index += 1
        
        print (f"{nums} / len(nums) = {len(nums)}  / nums.count('_') = { nums.count('_') }")
        return len(nums) - nums.count("_")
    
    
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    nums = [3,2,2,3]
    val = 3
    output = 2
    s.test(s.removeElement(nums,val),output) 
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    output = 5
    s.test(s.removeElement(nums,val),output) 
    
    nums = []
    val = 0
    output = 0
    s.test(s.removeElement(nums,val),output)
    
    nums = [2]
    val = 3
    output = 1
    s.test(s.removeElement(nums,val),output)
    
    #nums = [1,2,3,4]
    #index = 2
    #del nums[index]
    #nums.append("_")
    #print(nums)

if __name__ == "__main__":
    main()

    

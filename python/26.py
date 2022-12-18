
# numsの値もチェック対象になる。
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        index = 0
        for i in range(1,len(nums)):
            print (i,nums[index],nums[i])
            if (nums[index] !=nums[i] and nums[i] > nums[index]):
                index += 1
                nums[index] = nums[i]
                
                print (nums)
    
        print (nums)
        return index+1
        
            
        
        
def main():
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(nums)
    return s.removeDuplicates(nums)
    
        

if __name__ == "__main__":
    main()

    

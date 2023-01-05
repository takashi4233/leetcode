from typing import List
from typing import Optional

class Solution:
    # バイナリーサーチ(ちょっとは改善したけど、まだ遅い190ms / 36.96%)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]
        
    def binarySearch(self,nums,target,leftBias):
        left,right = 0,len(nums) -1
        i = -1
        while left <= right:
            m = (left + right) //2
            if target > nums[m]:
                left = m + 1
            elif target < nums[m]:
                right = m -1
            else:
                i = m
                if leftBias:
                    right = m -1
                else:
                    left = m + 1
        return i
        
    # 解けたけど、めちゃ遅い・・・？（239ms/5.28%)
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target and ans[0] == -1:
                ans[0] = left
            elif ans[0] == -1:
                left += 1

            if nums[right] == target and ans[1] == -1:
                ans[1] = right
            elif ans[1] == -1:
                right -= 1
            if ans[0] != -1 and ans[1] != -1:
                return ans
        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = [5,7,7,8,8,10]
    target = 8
    output = [3,4]
    s.test(s.searchRange(input,target),output)

    target = 6
    output = [-1,-1]
    s.test(s.searchRange(input,target),output)

    input = []
    target = 0
    output = [-1,-1]
    s.test(s.searchRange(input,target),output)

    input = [1,3]
    target = 1
    output = [0,0]
    print (input)
    s.test(s.searchRange(input,target),output)

    input = [1,2,3]
    target = 1
    output = [0,0]
    print (input)
    s.test(s.searchRange(input,target),output)



if __name__ == "__main__":
    main()


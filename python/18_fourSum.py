from typing import List
from typing import Optional

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i  in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                left = j+1
                right = len(nums)-1

                while left < right:
                    print (f"{nums[i]} + {nums[j]} + {nums[left]} + {nums[right]}")
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        a = [nums[i],nums[j],nums[left],nums[right]]
                        a.sort()
                        if a not in ans:
                            ans.append(a)
                        left += 1
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = [1,0,-1,0,-2,2]
    output = 0
    print (f"ans={s.fourSum(input,output)}")
    print ("[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]")

    input = [2,2,2,2,2]
    output = 8
    print (f"ans={s.fourSum(input,output)}")
    print ("[[2,2,2,2]]")


if __name__ == "__main__":
    main()


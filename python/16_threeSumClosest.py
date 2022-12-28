from typing import List
from typing import Optional

class Solution:
    # 15のthree sumと同じ2-pointer作戦。
    # 0ではなくtargetに近い方で移動させる
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = 10**5
        ans = 0
        for i,tmp in enumerate(nums):
            # 固定する数字が同じならパスする
            if i > 0 and tmp == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                threeSum = tmp + nums[left] + nums[right]
                if diff > abs(threeSum-target):
                    diff = abs(threeSum-target)
                    ans = threeSum
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    left += 1
                    ans = threeSum
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()

    nums = [-1,2,1,-4]
    target = 1
    output = 2
    s.test(s.threeSumClosest(nums,target),output)

    nums = [0,0,0]
    target = 1
    output = 0
    s.test(s.threeSumClosest(nums,target),output)

    nums =[-13,592,-501,770,-952,-675,322,-829,-246,657,608,485,-112,967,-30,182,-969,559,-286,-64,24,365,-158,701,535,-429,-217,28,948,-114,-536,-711,693,23,-958,-283,-700,-672,311,314,-712,-594,-351,658,747,949,70,888,166,495,244,-380,-654,454,-281,-811,-168,-839,-106,877,-216,523,-234,-8,289,-175,920,-237,-791,-976,-509,-4,-3,298,-190,194,-328,265,150,210,285,-176,-646,-465,-97,-107,668,892,612,-54,-272,-910,557,-212,-930,-198,38,-365,-729,-410,932,4,-565,-329,-456,224,443,-529,-428,-294,191,229,112,-867,-163,-979,236,-227,-388,-209,984,188,-549,970,951,-119,-146,801,-554,564,-769,334,-819,-356,-724,-219,527,-405,-27,-759,722,-774,758,394,146,517,870,-208,742,-782,336,-364,-558,-417,663,-914,536,293,-818,847,-322,408,876,-823,827,167]
    target = 7175
    output = 2921
    s.test(s.threeSumClosest(nums,target),output)



if __name__ == "__main__":
    main()


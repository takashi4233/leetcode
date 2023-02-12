from typing import List
from typing import Optional

class Solution:
    # バイナリーサーチ
    def search(self, nums: List[int], target: int) -> int:
        mid = (0 + len(nums)) //2
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+(high))//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
        return -1

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = [-1,0,3,5,9,12]
    target = 9
    output = 4
    s.test(s.search(input,target),output)

if __name__ == "__main__":
    main()


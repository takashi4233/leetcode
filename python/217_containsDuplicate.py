from typing import List
from typing import Optional

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = [1,2,3,1]
    output =  True
    s.test(s.containsDuplicate(input),output)

    input = [1,2,3,4]
    output =  False
    s.test(s.containsDuplicate(input),output)

    input = [1,1,1,3,3,4,3,2,4,2]
    output =  True
    s.test(s.containsDuplicate(input),output)



if __name__ == "__main__":
    main()


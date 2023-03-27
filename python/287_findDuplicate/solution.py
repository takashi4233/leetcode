from typing import List
from typing import Optional
from collections import Counter


class Solution:
    def findDuplicate２(self, nums: List[int]) -> int:
        counted = Counter(nums)
        duplicates = [item for item, count in counted.items() if count > 1]
        return duplicates[0]

    # フロイドの循環検出アルゴリズム
    def findDuplicate(self, nums):
        fast = nums[0]
        slow = nums[0]

        while True:
            print(f"fast={fast},slow={slow}")
            fast = nums[nums[fast]]
            slow = nums[slow]
            print(f"fast={fast},slow={slow}")
            if fast == slow:
                break

        slow = nums[0]
        print(f"slow={slow}")
        while slow != fast:
            print(f"fast={fast},slow={slow}")
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [1, 3, 4, 2, 2]
    output = 2
    sol.test(sol.findDuplicate(input), output)


if __name__ == "__main__":
    main()

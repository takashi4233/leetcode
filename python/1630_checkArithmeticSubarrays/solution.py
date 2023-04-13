from typing import List
from typing import Optional


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        res = []
        for s, e in zip(l, r):
            tmp = sorted(nums[s : e + 1])
            print(f"tmp={tmp}")
            base = tmp[1] - tmp[0]
            t = True
            for idx in range(2, len(tmp)):
                if base != tmp[idx] - tmp[idx - 1]:
                    t = False
                    break
            res.append(t)
        return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [4, 6, 5, 9, 3, 7]
    l, r = [0, 0, 2], [2, 3, 5]
    output = [True, False, True]
    sol.test(sol.checkArithmeticSubarrays(input, l, r), output)


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        k = len(nums)

        def dfs(path):
            if len(path) == k:
                ans.append(path.copy())
                return

            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs(path)
                    path.pop()

        dfs([])
        return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [1, 2, 3]
    output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    sol.test(sol.permute(input), output)


if __name__ == "__main__":
    main()

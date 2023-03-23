from typing import List
from typing import Optional


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(s: int, path: List[int]) -> None:
            print(f"s = {s},path = {path},ans = {ans}")
            if len(path) == k:
                ans.append(path.copy())
                return

            for i in range(s, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
        return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    n = 4
    k = 2
    output = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    sol.test(sol.combine(n, k), output)


if __name__ == "__main__":
    main()

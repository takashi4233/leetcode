from typing import List
from typing import Optional


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max_depth = len(triangle) - 2
        for i in range(max_depth, -1, -1):
            # print(f"i={i}")
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
            # print(triangle)

        return triangle[0][0]

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    output = 11
    sol.test(sol.minimumTotal(input), output)


if __name__ == "__main__":
    main()

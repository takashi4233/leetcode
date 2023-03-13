from typing import List
from typing import Optional


class Solution:
    # 163ms (26.55%)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = []
        max_area = 0

        def dfs(w, h):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                dx, dy = w + dx, h + dy
                if (
                    dx in range(rows)
                    and dy in range(cols)
                    and grid[dx][dy] != 0
                    and grid[dx][dy] < 2
                ):
                    grid[dx][dy] = 2
                    island.append([dx, dy])
                    dfs(dx, dy)
            # print(island)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island.append([r, c])
                    grid[r][c] = 2
                    dfs(r, c)
                    if max_area < len(island):
                        max_area = len(island)
                    island = []
        # print(max_area)
        # print(grid)
        return max_area

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    grid = [[1, 1, 0], [1, 0, 1], [1, 0, 1]]

    output = 4
    sol.test(sol.maxAreaOfIsland(grid), output)


if __name__ == "__main__":
    main()

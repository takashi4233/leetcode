from typing import List
from typing import Optional


class Solution:
    # 133ms (5.1%)　遅い
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rottened = []
        rotten = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rottened.append([r, c])

        def dfs() -> bool:
            is_changed = False
            direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for r, c in rottened:
                if grid[r][c] == 2:
                    for d in direction:
                        if (
                            0 <= r + d[0] < row
                            and 0 <= c + d[1] < col
                            and grid[r + d[0]][c + d[1]] == 1
                        ):
                            grid[r + d[0]][c + d[1]] = 2
                            is_changed = True
                            rotten.append([r + d[0], c + d[1]])
            return is_changed

        cnt = 0
        while dfs():
            cnt += 1
            rottened = rotten.copy()
            rotten = []
            # [Step1] Loopの回数を削減
            # 49ms(85.59%)
            # for r in range(row):
            #    for c in range(col):
            #        if grid[r][c] == 2:
            #            rottend.append([r, c])
            # print(f"cnt={cnt}:{grid}")

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1

        return cnt

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    output = 4
    sol.test(sol.orangesRotting(input), output)


if __name__ == "__main__":
    main()

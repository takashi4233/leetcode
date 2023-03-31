import collections
from typing import List
from typing import Optional


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dirs = [0, 1, 0, -1, 0]
        q = collections.deque()
        seen = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen[i][j] = True

        while q:
            i, j = q.popleft()
            for k in range(4):
                x = i + dirs[k]
                y = j + dirs[k + 1]
                if x < 0 or x == m or y < 0 or y == n:
                    continue
                if seen[x][y]:
                    continue
                mat[x][y] = mat[i][j] + 1
                q.append((x, y))
                seen[x][y] = True

        return mat

    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        dd = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 1:
                    near = []
                    for dx, dy in dd:
                        if c + dx in range(col) and r + dy in range(row):
                            near.append(mat[r + dy][c + dx])

                    if 0 not in near:
                        mat[r][c] = min(near) + 1
        return mat

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    ]
    output = [
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
        [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
        [3, 2, 2, 1, 0, 1, 0, 0, 1, 1],
    ]
    sol.test(sol.updateMatrix(input), output)


if __name__ == "__main__":
    main()

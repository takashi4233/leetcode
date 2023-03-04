from typing import List
from typing import Optional


class Solution:
    # refactor1と2で177ms(17.35%)から122ms(96.18%)に改善した
    def setZeroes(self, matrix: str) -> int:

        row = len(matrix)
        col = len(matrix[0])
        # [refactor 1]リストだと重複がでるのでSetにすべき
        # zero_r, zero_c = [], []
        zero_r, zero_c = set(), set()

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zero_r.add(r)
                    zero_c.add(c)

        # # [refactor 2]リストに全アクセスをしているので無駄が多い
        # for r in range(row):
        #     for c in range(col):
        #         if r in zero_r or c in zero_c:
        #             matrix[r][c] = 0
        for r in zero_r:
            for c in range(col):
                matrix[r][c] = 0
        for c in zero_c:
            for r in range(row):
                matrix[r][c] = 0

        return matrix

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    sol.test(sol.setZeroes(input), output)


if __name__ == "__main__":
    main()

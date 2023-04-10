from typing import List
from typing import Optional


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # 左上->一時領域へ
                top_left = matrix[top][l + i]
                # 左下→左上
                matrix[top][l + i] = matrix[bottom - i][l]
                # 右下→左下
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # 右上ｰ>右下
                matrix[bottom][r - i] = matrix[top + i][r]
                # 一時領域（左上）→右上
                matrix[top + i][r] = top_left
            l += 1
            r -= 1
        return matrix

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    sol.test(sol.rotate(input), output)


if __name__ == "__main__":
    main()

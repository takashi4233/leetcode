from typing import List
from typing import Optional


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # サイズを取得
        max_row, max_col = len(matrix), len(matrix[0])
        min_row, min_col = 0, 0
        # 進む方向
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        # 現在地
        c_row, c_col = 0, 0
        res.append(matrix[c_row][c_col])
        d = direct[0]

        while True:
            next_row, next_col = c_row + d[0], c_col + d[1]
            if min_row >= max_row or min_col >= max_row:
                # print(f"break")
                break
            elif min_row <= next_row < max_row and min_col <= next_col < max_col:
                # print(f"append,res={res}")
                res.append(matrix[next_row][next_col])
                c_row, c_col = next_row, next_col
            else:
                # print(f"change direction")
                if d == [0, 1]:
                    min_row += 1
                elif d == [1, 0]:
                    max_col -= 1
                elif d == [0, -1]:
                    max_row -= 1
                elif d == [-1, 0]:
                    min_col += 1
                i += 1
                d = direct[i % 4]
        return res

        # for d in direct:
        #     print(f"d={d}")
        #     next_row = c_row + d[0]
        #     next_col = c_col + d[1]
        #     print(
        #         f"1.c_row={c_row},c_col={c_col},n_row={next_row},n_col={next_col},res={res}"
        #     )
        #     # print(f"j={0 <= next_row < m_row and 0 <= next_col < m_col}")
        #     while 0 <= next_row < m_row and 0 <= next_col < m_col:
        #         # print(f"j={0 <= next_row < m_row},{ 0 <= next_col < m_col}")
        #         next_row = c_row + d[0]
        #         next_col = c_col + d[1]
        #         print(
        #             f"2.c_row={c_row},c_col={c_col},n_row={next_row},n_col={next_col},res={res}"
        #         )
        #         res.append(matrix[next_row][next_col])
        #         c_row, c_col = next_row, next_col
        #     # next_row = c_row - d[0]
        #     # next_col = c_col - d[1]

        # return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    sol.test(sol.spiralOrder(input), output)


if __name__ == "__main__":
    main()

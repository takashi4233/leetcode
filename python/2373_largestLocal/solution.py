from typing import List
from typing import Optional

class Solution:

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # 159ms / 85.37%
        # 処理を埋め込んだ方が早い
        def get_max_value(idx_x,idx_y)->int:
            return max(
                [
                    grid[idx_y][idx_x],grid[idx_y][idx_x+1],grid[idx_y][idx_x+2],
                    grid[idx_y+1][idx_x],grid[idx_y+1][idx_x+1],grid[idx_y+1][idx_x+2],
                    grid[idx_y+2][idx_x],grid[idx_y+2][idx_x+1],grid[idx_y+2][idx_x+2]
                ]
            )
        res = []
        matrix_size = len(grid)
        for idx_y in range(matrix_size-2):
            low = []
            for idx_x in range(matrix_size-2):
                low.append(get_max_value(idx_x,idx_y))
            res.append(low)
        return res

    # 287mx / 28.21%
    def largestLocal2(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        matrix_size = len(grid)
        for idx_y in range(matrix_size-2):
            low = []
            for idx_x in range(matrix_size-2):
                target = []
                for y in range(3):
                    for x in range(3):
                        target.append(grid[y+idx_y][x+idx_x])
                low.append(max(target))
            res.append(low)
        return res


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    output = [[9,9],[8,6]]
    s.test(s.largestLocal(grid),output)

if __name__ == "__main__":
    main()


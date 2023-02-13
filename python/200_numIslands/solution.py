from typing import List
from typing import Optional
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Gridのサイズ
        rows,cols = len(grid),len(grid[0])
        # 訪問済みの島の座標
        visit = set()
        # 島の数
        islands = 0
        
        # 幅優先探索
        def bfs(r,c):
            # 探索対象場所
            q = collections.deque()
            # 訪問済み島
            visit.add((r,c))
            # 対象を追加
            q.append((r,c))

            while q:
                # 取り出す
                row , col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                # 上下左右に移動しながら
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    # 縦横が範囲内かつ、島で、訪問したことがなければ
                    if (r in range(rows) and
                        c  in range(cols) and
                        grid[r][c]  == "1" and
                        (r , c) not in visit):
                        # qに追加する
                        q.append((r,c))
                        # 訪問済みにする
                        visit.add((r, c))


        for r in range(rows):
            for c in range(cols):
                # 座標が島で、訪れたことがなければ
                if grid[r][c] == "1" and (r,c) not in visit:
                    # 幅優先探索
                    bfs(r,c)
                    islands += 1

        return islands


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    output = 1
    s.test(s.numIslands(grid),output)

if __name__ == "__main__":
    main()


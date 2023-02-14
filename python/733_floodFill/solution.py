from typing import List
from typing import Optional

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return 0
        rows,cols = len(image),len(image[0])
        baseColor = image[sr][sc]

        def dfs(x,y):
            image[x][y]= color
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dx,dy in directions:
                dx , dy = x + dx , y + dy
                if  (
                    # imageの範囲内で
                    dx in range(rows) and dy in range(cols) and
                    # 未踏 あるいは 0でない
                    image[dx][dy] != color and image[dx][dy] == baseColor
                ):

                    dfs(dx,dy)
            return
        dfs(sr,sc)
        return image


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    output = [[2,2,2],[2,2,0],[2,0,1]]
    s.test(s.floodFill(image,sr,sc,color),output)

if __name__ == "__main__":
    main()


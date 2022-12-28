from typing import List
from typing import Optional

class Solution:
    # 速度を稼ぐために一回のループですべてのパターンの計算を実施した
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            row = []
            col = []
            box = []
            for j in range(0,9):
                if "." != board[j][i]:
                    if board[j][i] not in row:
                        row.append(board[j][i])
                    else:
                        return False

                if "." != board[i][j]:
                    if board[i][j] not in col:
                        col.append(board[i][j])
                    else:
                        return False

                if "." !=  board[(i%3)*3 + (j%3)][i//3*3 + j//3]:
                    if board[(i%3)*3 + (j%3)][i//3*3 + j//3] not in box:
                        box.append(board[(i%3)*3 + (j%3)][i//3*3 + j//3])
                    else:
                        return False
        return True
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    output = True
    s.test(s.isValidSudoku(board),output)       

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    output = False
    s.test(s.isValidSudoku(board),output)       


if __name__ == "__main__":
    main()

    

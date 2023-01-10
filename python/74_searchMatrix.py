from typing import List
from typing import Optional
import itertools

class Solution:
    
    #問題としては、BinarySearchで攻略すべきな気がする
    # 49ms (72.75%) Pythonの機能を使ったほうが早い・・・。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowSize = len(matrix)
        colSize = len(matrix[0])

        top = 0
        bottom = rowSize * colSize

        while top < bottom:
            middle = (top + bottom) // 2
            midVal =  matrix[middle//colSize][middle%colSize]
            if midVal == target:
                return True
            elif midVal < target:
                top = middle + 1
            else:
                bottom = middle
        return False

    # 43ms (91.25%)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        l = list(itertools.chain.from_iterable(matrix))
        return target in l

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    output = True
    s.test(s.searchMatrix(matrix,target),output)


    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    output = False
    s.test(s.searchMatrix(matrix,target),output)

if __name__ == "__main__":
    main()


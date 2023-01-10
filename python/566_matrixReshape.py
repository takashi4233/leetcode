from typing import List
from typing import Optional
import itertools
class Solution:
    # 91ms (86.36%)
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = list(itertools.chain.from_iterable(mat.copy()))
        if len(l) != r*c:
            return mat
        res = []
        tmp = []
        for idx in range(0,len(l)):
            tmp.append(l[idx])
            if idx % c == c-1 :
                res.append(tmp.copy())
                tmp.clear()
        return res

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    output = [[1,2,3,4]]
    s.test(s.matrixReshape(mat,r,c),output)
    
    mat = [[1,2],[3,4]]
    r = 2
    c = 4
    output = [[1,2],[3,4]]
    s.test(s.matrixReshape(mat,r,c),output)
    
    mat = [[1,2],[3,4]]
    r = 4
    c = 1
    output = [[1],[2],[3],[4]]
    s.test(s.matrixReshape(mat,r,c),output)

    mat = [[1,2]]
    r = 1
    c = 1
    output = [[1,2]]
    s.test(s.matrixReshape(mat,r,c),output)


if __name__ == "__main__":
    main()


from typing import List
from typing import Optional
import math

class Solution:
    # ニ項定理を使用
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for j in range(0,numRows):
            line=[]
            for i in range(0,j+1):
                line.append(self.comb(j,i))
            ans.append(line)
        return ans
    # 組合計算の関数を作る
    def comb(self,n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = 5
    output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    s.test(s.generate(input),output)       

    input = 1
    output = [[1]]
    s.test(s.generate(input),output)       


if __name__ == "__main__":
    main()

    

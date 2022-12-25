from typing import List
from typing import Optional
import math

class Solution:
    # ニ項定理を使用
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(0,rowIndex+1):
            ans.append(self.comb(rowIndex,i))
        return ans
    # 組合計算の関数を作る
    def comb(self,n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = 3
    output = [1,3,3,1]
    s.test(s.getRow(input),output)       

    input = 0
    output = [1]
    s.test(s.getRow(input),output)       

    input = 1
    output = [1,1]
    s.test(s.getRow(input),output)       


if __name__ == "__main__":
    main()

    

from typing import List
from typing import Optional

import math

class Solution:
    # log (x/y) = logx - logyの公式を使って解く
    # logで計算しているので、ezpで自然数に戻る
    # ただ、微妙な誤差で計算が合わないので、一旦保留
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        isMinus = False
        # logの値は正の数である必要があるので、答えの正負は最後に帳尻を合わせる
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) :
            isMinus = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        

        ans = int(math.exp(math.log(dividend) - math.log(divisor)))
        if isMinus:
            ans =  -1 * ans
        if ans > 2**31 - 1:
            return 2**31 -1
        if ans < -2**31:
            return -2**31
        return ans

    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    dividend = 10
    divisor = 3
    output = 3
    s.test(s.divide(dividend,divisor),output)  
    
    dividend = 0
    divisor = 1
    output = 0
    s.test(s.divide(dividend,divisor),output)    
    
    # dividend = -2147483648
    # divisor = -1
    # output = 2147483647
    # s.test(s.divide(dividend,divisor),output)
    
    dividend = 2147483647
    divisor = 1
    output = 2147483647
    s.test(s.divide(dividend,divisor),output)

    # 微妙な誤差で計算が合わない・・・。
    dividend = -231
    divisor = 3
    output = -77
    s.test(s.divide(dividend,divisor),output)



if __name__ == "__main__":
    main()

    

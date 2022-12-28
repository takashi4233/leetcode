from typing import List
# 問題としては面白みがないかなぁ。sqrt()を使ってはだめという縛りがあるけど、実際はそんなこと無いし。
# 回答もsqrt(x)が多くて、結果はいまいち
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        for i in range(0,x+1):
            if i * i == x:
                return i
            if i * i > x:
                return i-1
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = 4
    output = 2
    s.test(s.mySqrt(input),output)       
    
    input = 8
    output = 2
    s.test(s.mySqrt(input),output)    
    
    input = 1
    output = 1
    s.test(s.mySqrt(input),output)    
    
if __name__ == "__main__":
    main()

    

from typing import List
from typing import Optional

class Solution:
    # 文字列にキャストしてから並び替えてる。
    # 他社の解放を見ても、だいたいキャストしてる・・・。
    def reverse(self, x: int) -> int:
        isMinus=False
        if x < 0:
            isMinus=True
            x = abs(x)
        ans=int(str(x)[::-1])
        if isMinus:
            ans = -1* ans
        if ans > (2**31 -1) or ans < -2**31:
            return 0

        return ans
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = 123
    output = 321
    s.test(s.reverse(input),output)       


    input = -123
    output = -321
    s.test(s.reverse(input),output)       

    input = 120
    output = 21
    s.test(s.reverse(input),output)       



if __name__ == "__main__":
    main()

    

from typing import List
from typing import Optional

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        l = len(columnTitle)-1
        for i in range(0,len(columnTitle)):
#            print (f"{columnTitle[i]} = {ord(columnTitle[i]) -64}")
            ans += (ord(columnTitle[i]) -64) * (26 ** (l-i) )
        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = "A"
    output = 1
    s.test(s.titleToNumber(input),output)

    input = "AB"
    output = 28
    s.test(s.titleToNumber(input),output)

    input = "ZY"
    output = 701
    s.test(s.titleToNumber(input),output)

    input = "FXSHRXW"
    output = 2147483647
    s.test(s.titleToNumber(input),output)


if __name__ == "__main__":
    main()

    

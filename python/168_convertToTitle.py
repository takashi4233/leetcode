from typing import List
from typing import Optional
# 171の逆バージョン

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        tmp = []
        while columnNumber >= 27:
            a = columnNumber % 26
            if a == 0:
                a = 26
            tmp.append(a)
            columnNumber -= a
            columnNumber = columnNumber // 26
        tmp.append(columnNumber % 27)
        ans = ""
        for t in tmp[::-1]:
            ans += (chr(t+64))
        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 1
    output = "A"
    s.test(s.convertToTitle(input),output)

    input = 28
    output = "AB"
    s.test(s.convertToTitle(input),output)


    input = 701
    output = "ZY"
    s.test(s.convertToTitle(input),output)

    input = 52
    output = "AZ"   
    s.test(s.convertToTitle(input),output)



if __name__ == "__main__":
    main()


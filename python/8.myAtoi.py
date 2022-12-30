from typing import List
from typing import Optional
import re


class Solution:
    # 条件が複雑なので、一旦pending
    # atoiのをもう少し調べないと無理
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        s2 = re.search(r'[1-9]',s)
        print(s2)
        if not s2:
            return 0

        s = s.replace("+-","e")
        s = s.replace("-+","e")

        # # + or -より前の文字を消す
        # s2 = re.search(r'[+-]',s)
        # if s2 != None:
        #     #print (f"s2 = {s2.start()}")
        #     s = s[s2.start():len(s)]
        #     #print (f"s = {s}")
        
        # 条件0-3 -> 0
        p = re.compile(r"[0-9]-")
        print (f"m = {p.search(s)}")
        m = p.search(s)
        if m != None:
            return 0
        

        # p = re.compile(r"[0-9]+")
        # print (f"m = {p.search(s)}")
        # m = p.search(s)
        # if m != None:
        #     return 0

        
        s2 = re.search(r'[a-z.]',s)
        
        ans = 0
        if s2:
            s2 = s[0:s2.start()]
            if len(s2) == 0:
                ans =  0
            else:
                ans =  int(re.sub(r'[a-zA-Z\s]',"",s2))
        else:
            ans =  int(re.sub(r'[a-zA-Z\s]',"",s))
        
        #print (f"ans = {ans}")
        
        if ans >= 2**31-1:
            return 2**31 -1 
        elif ans <= -2**31:
            return -2**31
        else:
            return ans

    def test(self,input,answer):
        print (f"input = {input},answer = {answer}")
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = "42"
    output = 42
    s.test(s.myAtoi(input),output)

    input = "   -42"
    output = -42
    s.test(s.myAtoi(input),output)

    input = "4193 with words"
    output = 4193
    s.test(s.myAtoi(input),output)
	#英字の後の数字は認識できない。異常として０を出力する。
    input = "words and 987"
    output = 0
    s.test(s.myAtoi(input),output)
    #小数点以下は切り捨て
    input = "3.1415"
    output = 3
    s.test(s.myAtoi(input),output)
    
    input = "+-12"
    output = 0
    s.test(s.myAtoi(input),output)
    
    input ="00000-42a1234"
    output = 0
    s.test(s.myAtoi(input),output)
    
    input = "   +0 123"
    output = 0
    s.test(s.myAtoi(input),output)
    
if __name__ == "__main__":
    main()
from typing import List
from typing import Optional

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        while num > 0:
            if num >= 1000:
                ans = ans + "M"
                num -= 1000
            elif num >= 900:
                ans = ans + "CM"
                num -= 900
            elif num >= 500:
                ans = ans + "D"
                num -= 500 
            elif num >= 400:
                ans = ans + "CD"
                num -= 400
            elif num >= 100:
                ans = ans + "C"
                num -= 100
            elif num >= 90:
                ans = ans + "XC"
                num -= 90
            elif num >= 50:
                ans = ans + "L"
                num -= 50
            elif num >= 40:
                ans = ans + "XL"
                num -= 40
            elif num >= 10:
                ans = ans + "X"
                num -= 10
            elif num >= 9:
                ans = ans +"IX"
                num -= 9
            elif num >= 5:
                ans = ans + "V"
                num -= 5
            elif num >= 4:
                ans = ans + "IV"
                num -= 4
            elif num >= 1:
                ans = ans + "I"
                num -= 1

        
        return ans
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()

    input = 3
    output = "III"
    s.test(s.intToRoman(input),output)       

    input = 58
    output = "LVIII"
    s.test(s.intToRoman(input),output)       

    input = 1994
    output = "MCMXCIV"
    s.test(s.intToRoman(input),output)       


if __name__ == "__main__":
    main()

    

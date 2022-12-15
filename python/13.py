class Solution:
    def romanToInt(self, s: str) -> int:
        
        num = 0
        d = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for item1 in d.keys():
            if item1 in s:
                c = s.count(item1)
                num = num + d[item1] * c
                s = s.replace(item1,"-")
            
        return num
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
        
def main():
    
    
    s = Solution()
    s.test(s.romanToInt("III"),3)
    s.test(s.romanToInt("II"),2)
    s.test(s.romanToInt("LVIII"),58)
    s.test(s.romanToInt("MCMXCIV"),1994)
    s.test(s.romanToInt("MMMXLV"),3045)
    
    return ""
        
    
if __name__ == "__main__":
    main()

    

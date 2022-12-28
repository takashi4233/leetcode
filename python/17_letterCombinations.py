from typing import List
from typing import Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":["a","b","c"] , "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"],"9":["w","x","y","z"]}
        ans = []
        
        for digit in digits:
            if len(ans) == 0:
                ans = dic[digit]
            else:
                tmp = []
                for a in ans:
                    for d in dic[digit]:
                        tmp.append(a+d)
                ans = tmp
        return ans
        
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = "23"
    output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    s.test(s.letterCombinations(input),output)       

    input = ""
    output = []
    s.test(s.letterCombinations(input),output)       


    input = "2"
    output = ["a","b","c"]
    s.test(s.letterCombinations(input),output)       


if __name__ == "__main__":
    main()

    

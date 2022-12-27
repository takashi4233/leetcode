from typing import List
from typing import Optional
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = re.sub(r'[^a-zA-Z0-9]',"",s.lower())
        if tmp == tmp[::-1]:
            return True
        else:
            return False
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()

    input = "A man, a plan, a canal: Panama"
    output = True
    s.test(s.isPalindrome(input),output)       

    input = "race a car"
    output = False 
    s.test(s.isPalindrome(input),output)       


if __name__ == "__main__":
    main()

    

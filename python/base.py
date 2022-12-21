from typing import List
from typing import Optional

class Solution:
    def hogehoge(self, s: str) -> int: 
        print (s)
        return s
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = "hogehoge"
    output = 3
    s.test(s.hogehoge(input),output)       

if __name__ == "__main__":
    main()

    

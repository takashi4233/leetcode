from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:        
        return len(str.strip(s).split(" ")[-1])
        
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = "Hello World"
    output = 5
    s.test(s.lengthOfLastWord(input),output)       
    
    input = "   fly me   to   the moon  "
    output = 4
    s.test(s.lengthOfLastWord(input),output)       
    

    input = "luffy is still joyboy"
    output = 6
    s.test(s.lengthOfLastWord(input),output)       


if __name__ == "__main__":
    main()

    

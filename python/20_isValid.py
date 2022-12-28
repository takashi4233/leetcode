from typing import List
# なんとくイケてない気はする
class Solution:
    
    def isValid(self, s: str) -> bool:
        tmp = ""
        for i in range(0,len(s)):
            if len(tmp) == 0:
                tmp = tmp + s[i]
                continue
                
#            print (f"i = {i},tmp = {tmp}, tmp[-1] = {tmp[-1]} , s[i] = {s[i]}")
            if tmp[-1] == "(" and s[i] == ")":
                tmp = tmp[:-1]
                print (f"tmp = {tmp}")
                if len(tmp) == 0:
                    i += 1
                    continue
            
            elif tmp[-1] == ")" and s[i-1] != "(":
                return False

            
            elif tmp[-1] == "{" and s[i] == "}":
                tmp = tmp[:-1]
                if len(tmp) == 0:
                    i += 1
                    continue
            elif tmp[-1] == "}" and s[i-1] != "{":
                return False


            elif tmp[-1] == "[" and s[i] == "]":
                tmp = tmp[:-1]
                if len(tmp) == 0:
                    i += 1
                    continue
                
            elif tmp[-1] == "]" and s[i-1] != "[":
                return False

            else:
                tmp = tmp + s[i]

            i += 1

        if len(tmp) == 0:
            return True
        else :
            return False

            
    
    # {[]} = Trueに対応できない
    def isValid3(self, s: str) -> bool:
        for i in (0,len(s) -1):
            if s[i] == "(" and s[i+1] != ")":
                return False
            if s[i] == "{" and s[i+1] != "}":
                return False
            if s[i] == "[" and s[i+1] != "]":
                return False
            i += 1
        return True
    # ([)]　= False に対応できない
    def isValid2(self, s: str) -> bool:
        if s.count("(") != s.count(")"):
            return False
        if s.count("[") != s.count("]"):
            return False
        if s.count("{") != s.count("}"):
            return False
        return True
    
    def test(self,no,input,answer):
        assert input == answer, '{2} : 期待する値[{1}], 入力値[{0}]'.format(input, answer,no)
        
def main():
    s = Solution()
    i = 1
    input = "()"
    output = True
    s.test(i,s.isValid(input),output)       

    i  = 2
    input = "()[]{}"
    output = True
    s.test(i,s.isValid(input),output)       

    i = 3
    input = "(]"
    output = False
    s.test(i,s.isValid(input),output)  
    
    i = 4
    input = "([)]"
    output = False
    s.test(i,s.isValid(input),output) 
    
    i = 5
    input = "{[]}" 
    output = True
    s.test(i,s.isValid(input),output) 

if __name__ == "__main__":
    main()
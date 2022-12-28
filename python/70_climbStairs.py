from typing import List
class Solution:
    # [1,2,3,4,5,6] -> [1,2,3,5,8,13] steps
    # フィボナッチ数になっていると予想
    def climbStairs(self, n: int) -> int:
        num1 = 0
        num2 = 1
        
        for i in range(0,n):
            tmp = num2
            num2 = num1 + num2
            num1 = tmp
            
        return num2
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = 2
    output =2
    s.test(s.climbStairs(input),output)       
    
    input = 3
    output = 3
    s.test(s.climbStairs(input),output)    
    
    input = 6
    output = 13
    s.test(s.climbStairs(input),output)    
    
    

if __name__ == "__main__":
    main()

    

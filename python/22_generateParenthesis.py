from typing import List
from typing import Optional

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def rec(left,right,stack,ans):
            if left == right == 0:
                output.append(ans)
                return
            if left > 0:
                rec(left-1,right,stack+1,ans+"(")

            if right > 0 and stack > 0:
                rec(left,right-1,stack-1,ans+")")

        rec(n,n,0,"")
        return output

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 3
    output = ["((()))","(()())","(())()","()(())","()()()"]
    s.test(s.generateParenthesis(input),output)

    input = 1
    output = ["()"]
    s.test(s.generateParenthesis(input),output)

if __name__ == "__main__":
    main()


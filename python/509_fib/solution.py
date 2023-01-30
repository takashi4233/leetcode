from typing import List
from typing import Optional

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        t1 , t2 = 0,1
        for i in range(2,n+1):
            t1,t2 = t2,t1+t2
        return t2

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 2
    output = 1
    s.test(s.fib(input),output)

if __name__ == "__main__":
    main()


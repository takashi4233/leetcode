from typing import List
from typing import Optional

class Solution:
    # トリボナッチ数（フィボナッチの３つ番）
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        t1 = 0
        if n < 2:
            return 1
        t2 = 1
        t3 = 1
        for i in range(3,n+1):
            t1,t2,t3  = t2,t3,t1+t2+t3
        return t3


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 4
    output = 4
    s.test(s.tribonacci(input),output)

if __name__ == "__main__":
    main()


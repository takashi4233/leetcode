from typing import List
from typing import Optional

class Solution:
    #お、、、遅いぞ126ms /5.4%
    def isPowerOfTwo(self, n: int) -> bool:
        while n  > 0:
            if n == 1:
                return True
            n = n // 2
        return False

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 16
    output = True
    s.test(s.isPowerOfTwo(input),output)

if __name__ == "__main__":
    main()


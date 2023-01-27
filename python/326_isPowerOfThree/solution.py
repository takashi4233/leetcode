from typing import List
from typing import Optional
import math

class Solution:

    # 83ms (77.24%)
    #　Logってこんな使い方があるのか・・・・。
    # n = 3^i
    # i = log3(n)
    # i = log(n) / log(3)
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        log_base_3 = math.log(n, 3)
        return 3 ** round(log_base_3) == n


    # お、、、遅いぞ・・・。7552ms 5.5%
    def isPowerOfThree2(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n/3)

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 27
    output = True
    s.test(s.isPowerOfThree(input),output)

if __name__ == "__main__":
    main()


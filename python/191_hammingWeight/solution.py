from typing import List
from typing import Optional

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 0b0000000000000000000000000001011
    output = 3
    s.test(s.hammingWeight(input),output)

if __name__ == "__main__":
    main()


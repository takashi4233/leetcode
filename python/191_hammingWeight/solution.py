from typing import List
from typing import Optional

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    # 2進数なら0b , 8進数なら0o, 16進数なら0xをつければOK
    input = 0b00000000000000000000000000001011
    output = 3
    s.test(s.hammingWeight(input),output)

if __name__ == "__main__":
    main()


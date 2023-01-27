from typing import List
from typing import Optional

class Solution:
    def reverseBits(self, n: int) -> int:
        res    = 0
        for i in range(32):
            if n&1:
                res += 1 << (31-i)
            #bit shift
            # a = 60  #0011 1100 
            # r = a >> 2
            # r = 0000 1111
            n >>= 1
            
        return res

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 0b00000010100101000001111010011100
    output = 964176192
    s.test(s.reverseBits(input),output)

if __name__ == "__main__":
    main()


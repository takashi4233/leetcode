from typing import List
from typing import Optional

class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) != 1:
            tmp = 0
            for w in s:
                tmp += int(w)
            s = str(tmp)
        return int(s)

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = 38
    output = 2
    s.test(s.addDigits(input),output)

    input = 0
    output = 0
    s.test(s.addDigits(input),output)


if __name__ == "__main__":
    main()


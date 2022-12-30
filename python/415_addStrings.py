from typing import List
from typing import Optional

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    num1 = "11"
    num2 = "123"
    output = "134"
    s.test(s.addStrings(num1,num2),output)

    num1 = "456"
    num2 = "77"
    output = "533"
    s.test(s.addStrings(num1,num2),output)

    num1 = "0"
    num2 = "0"
    output = "0"
    s.test(s.addStrings(num1,num2),output)

if __name__ == "__main__":
    main()


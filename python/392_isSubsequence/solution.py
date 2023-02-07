from typing import List
from typing import Optional

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for w in s:
            print (f"w={w},t={t}")
            if w not in t:
                return False
            t = t[t.find(w)+1:]
        return True

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = "abc"
    input2 = "ahbgdc"
    output = True
    s.test(s.isSubsequence(input,input2),output)

if __name__ == "__main__":
    main()


from typing import List
from typing import Optional
from collections import Counter


class Solution:
    # 91ms (90.55%)
    def firstUniqChar(self, s: str) -> int:
        words = list(s)
        d = Counter(words)
        for i in range(0,len(words)):
            if d[words[i]] == 1:
                return i
        return -1

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = "leetcode"
    output = 0
    s.test(s.firstUniqChar(input),output)

    input = "loveleetcode"
    output = 2
    s.test(s.firstUniqChar(input),output)

    input = "aabb"
    output = -1
    s.test(s.firstUniqChar(input),output)

if __name__ == "__main__":
    main()


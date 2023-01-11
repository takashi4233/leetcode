from typing import List
from typing import Optional
from collections import Counter

class Solution:
    # 50ms (88.66%)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dr = Counter(ransomNote)
        dm = Counter(magazine)
        for w in dr:
            if dm[w] < dr[w]:
                return False
        return True

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    ransomNote = "a"
    magazine = "b"
    output = False
    print(ransomNote)
    s.test(s.canConstruct(ransomNote,magazine),output)

    ransomNote = "aa"
    magazine = "ab"
    output = False
    print(ransomNote)
    s.test(s.canConstruct(ransomNote,magazine),output)

    ransomNote = "aa"
    magazine = "aab"
    output = True
    print(ransomNote)
    s.test(s.canConstruct(ransomNote,magazine),output)
    
    ransomNote = "aab"
    magazine = "baa"
    output = True
    print(ransomNote)
    s.test(s.canConstruct(ransomNote,magazine),output)


if __name__ == "__main__":
    main()


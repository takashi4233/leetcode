from typing import List
from typing import Optional

class Solution:
    # 57ms (69.15ms)
    def isAnagram(self, s: str, t: str) -> bool:
        
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()

        return sl ==  tl


def main():
    s = "anagram"
    t = "nagaram"
    output = True
    print (s.isAnagram(s,t))

    s = "rat"
    t = "car"
    output = False
    print (s.isAnagram(s,t))


if __name__ == "__main__":
    main()


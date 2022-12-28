from typing import List
from typing import Optional

class Solution:
    # 解放としてはつまらないけど、Pythonを使ってるなら妥当な回答な気がする。
    # 40ms(71.66%)
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    
    haystack = "sadbutsad"
    needle = "sad"
    output = 0
    s.test(s.strStr(haystack,needle),output)       

    haystack = "leetcode"
    needle = "leeto"
    output = -1
    s.test(s.strStr(haystack,needle),output)       


if __name__ == "__main__":
    main()

    

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        index = 1
        # リストに１つしか単語が含まれないなら、その文字が答え
        if len(strs) == 1:
            return strs[0]
        # リストの先頭の文字が""なら、こたえは""
        # 正しくは、リストのどれか一つでもだと思う
        if len(strs[0]) == 0:
            return ""
        # リストの先頭の文字列の１文字目を選ぶ
        s = strs[0][0]
        while True:
            for st in strs:
                if not st.startswith(s):
                    return s[0:index-1]
            index = index + 1
            if index > len(strs[0]):
                return s
            s = strs[0][0:index]
        return s
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    
    # Prefixで有ることを忘れてた・・・。
    input = ["c","acc","ccc"]
    output = ""
    s.test(s.longestCommonPrefix(input),output)       

    
    input = ["flower","flower","flower","flower"]
    output = "flower"
    s.test(s.longestCommonPrefix(input),output)       


    input = ["a"]
    output = "a"
    s.test(s.longestCommonPrefix(input),output)       


    input = [""]
    output = ""
    s.test(s.longestCommonPrefix(input),output)       
    
    
    input = ["flower","flow","flight"]
    output = "fl"
    s.test(s.longestCommonPrefix(input),output)       

    input = ["dog","racecar","car"]
    output = ""
    s.test(s.longestCommonPrefix(input),output)       


if __name__ == "__main__":
    main()

    

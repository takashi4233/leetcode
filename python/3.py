class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = s[0:1]

        a = 1
        for c in s[1:]:
            if c in ans:
                ans = ans.split(c)[1] + c
            else :
                ans = ans + c
                if (a < len(ans)):
                    a = len(ans)
        return a



def main():
    q = "abcabcdd"
    s = Solution()
    a = s.lengthIfLongestSubstring(q)
    print(a)
    


        

if __name__ == "__main__":
    main()

    

        

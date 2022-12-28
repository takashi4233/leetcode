class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                tmp1 = s[i:j]
                tmp2 = s[i:j]
                tmp2 = tmp2[::-1]
                print (f"tmp1 = {tmp1} / tmp2 = {tmp2}")    
                if tmp1 == tmp2 and len(tmp1) > len(ans):
                    ans = tmp1
        return ans
                


def main():
    s = Solution()
        
    print ("----------")
    input = "cbbd"
    print(f"Q {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")
    input = "abcbe"
    print(f"Q {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")
    input = "aacabdkacaa"
    print(f"Q {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")
    input = "babad"
    print(f"Q1 {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")
    input = "cbbd"
    print(f"Q2 {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")
    input = "ac"
    print(f"Q3 {input}")
    print(f"ans:{s.longestPalindrome(input)}")

    print ("----------")    
    input = "abb"
    print(f"Q4 {input}")
    print(f"ans:{s.longestPalindrome(input)}")

    print ("----------")    
    input = "ccd"
    print(f"Q5 {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")    
    input = "eabcb"
    print(f"Q6 {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
    print ("----------")    
    input = "abb"
    print(f"Q {input}")
    print(f"ans:{s.longestPalindrome(input)}")

    print ("----------")    
    input = "ccb"
    print(f"Q {input}")
    print(f"ans:{s.longestPalindrome(input)}")
    
if __name__ == "__main__":
    main()

    



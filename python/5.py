class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 2:
            if (s[0] == s[1]):
                return s
            else:
                return s[0] 
        
        if len(s) == 3:
            if s[0] == s[2]:
                return s
            else:
                s2 = s[::-1]
                print (s)
                print (s2)
                ans = ""
                tmp = ""
                for i in range(0,len(s)):
                    if (s[i] == s2[i]):
                        tmp = tmp + s[i]
                        #if (tmp != tmp[::-1]):
                        #    tmp = ""
                    else:
                        tmp = ""
                    if len(tmp) > len(ans):
                        ans = tmp
                        print (f"1.{ans}")
                
        if s == s[::-1]:
            return s
        
        s2 = s[::-1]
        print (s)
        print (s2)
        ans = ""
        tmp = ""
        for i in range(0,len(s)):
            if (s[i] == s2[i]):
                tmp = tmp + s[i]
                #if (tmp != tmp[::-1]):
                #    tmp = ""
            else:
                tmp = ""
            if len(tmp) > len(ans):
                ans = tmp
                print (f"1.{ans}")
        
        if ans != ans[::-1]:
            ans = ""
        
        s1 = s
        s2 = s[::-1]
        for j in range(0,len(s)):
            s1 = s1+ "-"
            s2 = s1[::-1]
            tmp = ""
            
            for i in range(0,len(s1)):
                if (s1[i] == s2[i]):
                    tmp = tmp + s1[i]
                else:
                    tmp = ""
                if len(tmp) > len(ans):
                    ans = tmp
                    print (f"2.{ans}/{j}")

        s1 = s
        s2 = s[::-1]                   
        for j in range(0,len(s)):
            s1 = "-" + s1
            s2 = s1[::-1]
            
            tmp = ""
            for i in range(0,len(s1)):
                if (s1[i] == s2[i]):
                    tmp = tmp + s1[i]
                else:
                    tmp = ""
                if len(tmp) > len(ans):
                    ans = tmp
                    print (f"3.{ans}/{j}")
        return ans
        


def main():
    s = Solution()

    print ("----------")
    input = "abcdbbfcba"
    output = s.longestPalindrome(input)
    print(f"Q {input}")
    if output == "bb":
        print ("OK")
    else:
        print ("NG")
        print(f"ans:{output}")
    
    return
    
    
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

    



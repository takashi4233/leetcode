from typing import List
from typing import Optional
from collections import Counter

class Solution:
    # 25ms / 97.79ms
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        # 文字ごとに辞書型に格納する
        count = Counter(s)

        # 一文字ずつみて、偶数ならその数を奇数なら１を引いた数（最大偶数）の総和を取る
        for c in count.values():
            ans += c if c % 2 == 0 else c -1
        # 一文字でも奇数があったかを確認する
        # anyはリストの中で１つでもTrueがあればTrueを返す
        # 逆はall()
        hasoddcount = any(c % 2 == 1 for c in count.values())

        return ans+ hasoddcount

    # 40ms / 38.81ms
    def longestPalindrome2(self, s: str) -> int:
        d = {}
        ans = 0
        for w in s:
            if w not in d:
                d[w] = 1
            else:
                d[w] += 1

        for key,val in d.items():
            ans += val//2 * 2
            d[key] = d[key] - val//2 * 2
        
        for val in d.values():
            if val > 0:
                ans += 1
                break

        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = "abccccdd"
    output = 7  
    s.test(s.longestPalindrome(input),output)

if __name__ == "__main__":
    main()


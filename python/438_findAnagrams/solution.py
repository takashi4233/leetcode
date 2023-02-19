from typing import List
from typing import Optional


class Solution:
    # ハッシュマップを使って比較。
    # Pythonはハッシュマップをそのまま比較できる。
    # 110ms / 81.31%
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        if pCount == sCount:
            res = [0]
        else:
            res = []

        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if pCount == sCount:
                res.append(l)
        return res

    # 9240ms(5.3%) Clearだけど激遅い
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        ans = []
        # pをアルファベット順に並び替える
        p = "".join(sorted(p))
        #        print(p)
        #        print(f"slen={s_len},plen={p_len}")
        for i in range(s_len - p_len + 1):
            tmp = "".join(sorted(s[i : i + p_len]))
            #            print(f"[{i}] tmp={tmp}")
            if tmp == p:
                ans.append(i)
        return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()
    input = "cbaebabacd"
    p = "abc"
    output = [0, 6]
    s.test(s.findAnagrams(input, p), output)


if __name__ == "__main__":
    main()

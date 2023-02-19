from typing import List
from typing import Optional


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            # ハッシュに値を格納する
            count[s[r]] = 1 + count.get(s[r], 0)
            # 窓のサイズから、最頻出文字のサイズを引いて、それがK以上なら
            # while (r - l + 1) - max(count.values()) > k:
            if (r - l + 1) - max(count.values()) > k:
                # 窓の左側の文字を消して
                count[s[l]] -= 1
                # 窓の左側を一つづらす
                l += 1
            res = max(res, r - l + 1)
        return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()
    input = "ABAB"
    k = 2
    output = 4
    s.test(s.characterReplacement(input, k), output)


if __name__ == "__main__":
    main()

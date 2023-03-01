from typing import List
from typing import Optional
import collections


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = []
        # 文字数分の空白の箱を用意する
        bucket = [[] for _ in range(len(words) + 1)]
        # counterを使うことで文字と頻度が取得できる
        for word, freq in collections.Counter(words).items():
            bucket[freq].append(word)
        # 逆順（頻度が高い順に並び替えて）
        for b in reversed(bucket):
            # 同じ頻度で出現した文字は辞書順で並び替える
            for word in sorted(b):
                ans.append(word)
                if len(ans) == k:
                    return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    output = ["i", "love"]
    sol.test(sol.topKFrequent(words, k), output)


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            # 文字列の並び替え（ソート）
            sorted_str = "".join(sorted(str))
            print(f"{sorted_str}")
            # 辞書型変数にリストを追加する
            d.setdefault(sorted_str, []).append(str)

        return d.values()
        # 上の一行で下の４行分の処理ができる
        # ans = []
        # for v in d.values():
        #    ans.append(v)
        # return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    sol.test(sol.groupAnagrams(input), output)


if __name__ == "__main__":
    main()

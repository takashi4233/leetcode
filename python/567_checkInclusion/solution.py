from typing import List
from typing import Optional
from collections import Counter


class Solution:
    # 1403ms (20.94%)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word_length = len(s1)
        s1_dic = Counter(s1)
        size = len(s2) - word_length + 1

        # [Step1]評価の回数を減らす
        # 1403ms (20.94%) -> 1347ms (23.12%)
        # for i in range(len(s2) - word_length + 1):
        for i in range(size):
            t = s2[i : i + word_length]
            s2_dic = Counter(t)
            # print(f"s1_dic={dict(s1_dic)},s2_dic={dict(s2_dic)}")

            # [Step2] 辞書型への変換をやめる。効果なし
            # 1347ms (23.12%) -> 1341ms(23.39%)
            # if dict(s1_dic) == dict(s2_dic):
            #
            if s1_dic == s2_dic:
                return True
        return False

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    s1 = "adc"
    s2 = "dcda"
    output = True
    sol.test(sol.checkInclusion(s1, s2), output)


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional

class Solution:
    # それぞれの文字列で文字の出現順を比較することで同形文字を抽出する
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input1,input2 = "egg","add"
    output = True
    s.test(s.isIsomorphic(input1,input2),output)

if __name__ == "__main__":
    main()


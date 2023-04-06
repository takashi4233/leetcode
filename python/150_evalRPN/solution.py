from typing import List
from typing import Optional
import re


class Solution:
    # 153ms(5.8%) isdigitの判断に時間を割きすぎ
    def evalRPN2(self, tokens: List[str]) -> int:
        n = []
        pattern = r"^[-]?\d+(?:\.\d+)?$"
        for token in tokens:
            # print(f"token={token},n={n}")
            if re.match(pattern, token):
                n.append(token)
            else:
                n1 = n.pop()
                n2 = n.pop()
                n.append(int(eval(f"{n2}{token}{n1}")))
        return int(n.pop())

    # 53ms(99.71%)
    def evalRPN(self, tokens: List[str]) -> int:
        n = []
        for t in tokens:
            # +と*は前後関係に依存しない
            if t == "+":
                n.append(n.pop() + n.pop())
            elif t == "*":
                n.append(n.pop() * n.pop())
            # -と/は前後関係があるので、一時変数を使う
            elif t == "-":
                a, b = n.pop(), n.pop()
                n.append(b - a)
            elif t == "/":
                a, b = n.pop(), n.pop()
                n.append(int(b / a))
            else:
                # 演算子の処理を最初にすることで、数字の判断が不要になる
                n.append(int(t))
        return n.pop()

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = ["18"]
    output = 18
    sol.test(sol.evalRPN(input), output)


if __name__ == "__main__":
    main()

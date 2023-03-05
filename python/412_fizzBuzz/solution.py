from typing import List
from typing import Optional


class Solution:
    # 44ms(64.11%)だけど、最速のコードを見ても同じ。
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(f"{str(i)}")
        return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = 3
    output = ["1", "2", "Fizz"]
    sol.test(sol.fizzBuzz(input), output)


if __name__ == "__main__":
    main()

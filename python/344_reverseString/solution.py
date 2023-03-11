from typing import List
from typing import Optional


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = ["h", "e", "l", "l", "o"]
    output = ["o", "l", "l", "e", "h"]
    sol.test(sol.reverseString(input), output)


if __name__ == "__main__":
    main()

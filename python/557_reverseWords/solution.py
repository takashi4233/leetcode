from typing import List
from typing import Optional


class Solution:
    #   31ms (90.98%)
    def reverseWords(self, s: str) -> str:
        ans = []
        words = s.split(" ")
        for word in words:
            ans.append(word[::-1])
        return " ".join(ans)

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = "Let's take LeetCode contest"
    output = "s'teL ekat edoCteeL tsetnoc"
    sol.test(sol.reverseWords(input), output)


if __name__ == "__main__":
    main()

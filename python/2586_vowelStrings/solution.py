from typing import List
from typing import Optional


class Solution:
    # 71ms(49.7%)
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        words = words[left : right + 1]
        # print(f"words={words}")
        cnt = 0
        v = ("a", "i", "u", "e", "o")
        for word in words:
            if word[0] in v and word[-1] in v:
                cnt += 1
        return cnt

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = ["are", "amy", "u"]
    left, right = 0, 2
    output = 2
    sol.test(sol.vowelStrings(input, left, right), output)


if __name__ == "__main__":
    main()

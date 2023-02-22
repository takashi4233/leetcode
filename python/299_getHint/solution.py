from typing import List
from typing import Optional


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        # 0 - 9 までのスペースを用意する
        bucket = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                bucket[int(s)] += 1
                bucket[int(g)] -= 1

        return f"{bulls}A{len(secret) - bulls - sum(x for x in bucket if x > 0)}B"

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()
    secret = "1807"
    guess = "7810"

    output = "1A3B"
    s.test(s.getHint(secret, guess), output)


if __name__ == "__main__":
    main()

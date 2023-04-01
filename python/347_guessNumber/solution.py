from typing import List
from typing import Optional


class Solution:
    def guess(self, num):
        if num == 6:
            return 0
        elif num < 6:
            return 1
        else:
            return -1

    def guessNumber(self, n: int) -> int:
        low, height = 0, n
        while True:
            mid = (low + height) // 2
            a = self.guess(mid)
            # print(f"a = {a},low={low},height={height}")
            if a == 0:
                return mid
            elif a == -1:
                height = mid
            elif a == 1:
                low = mid + 1

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = 10
    output = 6
    sol.test(sol.guessNumber(input), output)


if __name__ == "__main__":
    main()

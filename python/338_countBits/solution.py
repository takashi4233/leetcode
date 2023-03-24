from typing import List
from typing import Optional


class Solution:
    # 94ms(49.9%)
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            # 不要なキャストを削除85ms(70.73%)
            # count()はStr型にしか使えないが、binしたらstr型になってる模様
            # res.append(str(bin(i)).count("1"))
            res.append(bin(i).count("1"))
        return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = 2
    output = [0, 1, 1]
    sol.test(sol.countBits(input), output)


if __name__ == "__main__":
    main()

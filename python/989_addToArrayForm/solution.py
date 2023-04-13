from typing import List
from typing import Optional


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a, sum = 1, 0
        while num:
            sum += a * num.pop()
            a *= 10
        return list(map(int, list(str(sum + k))))

    # 各桁の合計値が10を超えたときに対応できない
    def addToArrayForm2(self, num: List[int], k: int) -> List[int]:
        kl = list(str(k))
        tmp = len(kl) - len(num)
        if tmp > 0:
            num = [0] * tmp + num
        elif tmp < 0:
            kl = [0] * abs(tmp) + kl
        # print(f"kl={kl},num={num}")
        return [a + int(b) for a, b in zip(num, kl)]

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    num = [1, 2, 0, 0]
    k = 34
    output = [1, 2, 3, 4]
    sol.test(sol.addToArrayForm(num, k), output)


if __name__ == "__main__":
    main()

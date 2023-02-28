from typing import List
from typing import Optional


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            print(f"stones = {stones}")
            first = stones.pop(0)
            second = stones.pop(0)
            # この処理はなくても良い
            # if first == second:
            #    continue
            if first != second:
                new_num = first - second
                stones.append(new_num)
                stones.sort(reverse=True)
        if len(stones) == 1:
            return stones.pop()
        else:
            return 0

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    output = 1
    sol.test(sol.lastStoneWeight(stones), output)


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []  # decreasing stack常に単調減少になる

        for i, temperature in enumerate(temperatures):
            # print(f"i={i},temperature={temperature},stack={stack} ans={ans}")

            while stack and temperature > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index

            stack.append(i)

        return ans

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [1, 1, 4, 2, 1, 1, 0, 0]
    sol.test(sol.dailyTemperatures(input), output)


if __name__ == "__main__":
    main()

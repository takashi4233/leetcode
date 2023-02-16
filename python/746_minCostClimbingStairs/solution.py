from typing import List
from typing import Optional


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        p1_pos, p1_val = 0, cost[0]
        p2_pos, p2_val = 1, cost[1]
        print(
            f"len={len(cost)},p1_pos={p1_pos},p1_val={p1_val},p2_pos={p2_pos},p2_val={p2_val}"
        )
        while p1_pos + 2 < len(cost) and p2_pos + 2 < len(cost):
            print(f"p1_pos={p1_pos},p1_val={p1_val},p2_pos={p2_pos},p2_val={p2_val}")
            if p1_val <= p2_val:
                # if cost[p1_pos + 1] == cost[p1_pos + 2]:
                #     p1_pos += 2
                #     p1_val += cost[p1_pos]

                if cost[p1_pos + 1] >= cost[p1_pos + 2]:
                    p1_pos += 2
                    p1_val += cost[p1_pos]
                else:
                    p1_pos += 1
                    p1_val += cost[p1_pos]
            else:
                # if cost[p2_pos + 1] == cost[p2_pos + 2]:
                #     p2_pos += 2
                #     p2_val += cost[p2_pos]
                if cost[p2_pos + 1] >= cost[p2_pos + 2]:
                    p2_pos += 2
                    p2_val += cost[p2_pos]
                else:
                    p2_pos += 1
                    p2_val += cost[p2_pos]
        print(f"p1_pos={p1_pos},p1_val={p1_val},p2_pos={p2_pos},p2_val={p2_val}")
        if p1_pos + 2 >= len(cost) and p2_pos + 2 >= len(cost):
            return min(p1_val, p2_val)
        elif p1_pos + 2 >= len(cost):
            return p1_val
        else:
            return p2_val

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    s = Solution()
    cost = [10, 15, 20]
    output = 15
    s.test(s.minCostClimbingStairs(cost), output)


if __name__ == "__main__":
    main()

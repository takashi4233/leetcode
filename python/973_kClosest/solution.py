from typing import List
from typing import Optional
import math


class Solution:
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        for l in points:
            print(l)

    # memo:たぶん、近い順にk個の値を返せばよいと思う
    # 実装がまずい気がする
    # class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict = {}
        for l in points:
            print(f"l={l}")
            # key = l[0] * l[0] + l[1] * l[1]
            key = l[0] ** 2 + l[1] ** 2
            if key not in dict:
                dict[key] = []
            dict[key].append(l)
        dict2 = sorted(dict.items())
        print(f"res={dict2}")
        res = []
        cnt = 0
        for d in dict2:
            for v in d[1]:
                res.append(v)
            if len(res) == k:
                return res

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [[1, 3], [-2, 2]]
    k = 1
    output = [[-2, 2]]
    sol.test(sol.kClosest(input, k), output)


if __name__ == "__main__":
    main()

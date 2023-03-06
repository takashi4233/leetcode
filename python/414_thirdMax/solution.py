from typing import List
from typing import Optional


class Solution:
    # 62ms(28.48%) 遅い？
    def thirdMax(self, nums: List[int]) -> int:
        # [Step1]降順ソートは不要。結構効く
        # 62ms(28.48%)  -> 53ms(76.74%)
        # l = sorted(list(set(nums)), reverse=True)
        l = sorted(list(set(nums)))
        # [Step2] if判定をせずにtry,exceptを使うと更に高速に
        # 53ms(76.74%) -> 46ms(96.25%)
        # if len(l) < 3:
        #    return max(l)
        # return l[2]
        try:
            return l[-3]
        except:
            return max(l)

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    input = [3, 2, 1]
    output = 1
    sol.test(sol.thirdMax(input), output)


if __name__ == "__main__":
    main()

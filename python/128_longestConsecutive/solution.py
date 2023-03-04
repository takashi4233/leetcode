from typing import List
from typing import Optional


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # setを使うことで重複を排除できる
        #  420ms(57.1%) -> 394ms(59.5%)
        # nums_sort = sorted(nums)
        nums_sort = sorted(list(set(nums)))
        # 本来はsortせずに、対象数字の+1がリスト（Set）に含まれているかでチェックする
        n = nums_sort[0]
        cnt, max_cnt = 1, 0
        # 余計なprintを削除で394ms(59.5%) -> 305ms(96.75%)
        # print(nums_sort)
        for i in range(1, len(nums_sort)):
            # setで重複を排除したので、この処理は不要
            # 305ms(96.75%) -> 302ms(97.99%)
            # if nums_sort[i] == n:
            #    continue
            if nums_sort[i] - n == 1:
                # 余計なprintを削除で394ms(59.5%) -> 305ms(96.75%)
                # print(f"n = {n},sort={nums_sort[i]}")
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
            n = nums_sort[i]
        if max_cnt < cnt:
            return cnt
        else:
            return max_cnt

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    output = 4
    sol.test(sol.longestConsecutive(nums), output)


if __name__ == "__main__":
    main()

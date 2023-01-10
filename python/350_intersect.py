from typing import List
from typing import Optional
from collections import Counter
class Solution:
    # Counter(Counterは辞書型dictのサブクラスで、キーに要素、値に出現回数という形のデータを持つ。)
    # 48ms / 89.53%
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret_arr = []
        d = Counter(nums1)
        for num in nums2:
            if d[num] > 0:
                ret_arr.append(num)
                d[num] -= 1
        return ret_arr
    
    # 70ms / 61.23%
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        if len(nums1) < len(nums2):
            for n in nums1:
                if n in nums2:
                    ans.append(n)
                    nums2.remove(n)
        else:
            for n in nums2:
                if n in nums1:
                    ans.append(n)
                    nums1.remove(n)
        return ans

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    output = [2,2]
    s.test(s.intersect(nums1,nums2),output)

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    output = [4,9]
    s.test(s.intersect(nums1,nums2),output)
    
    nums1 = [1,2]
    nums2 = [1,1]
    output = [1]
    s.test(s.intersect(nums1,nums2),output)


if __name__ == "__main__":
    main()


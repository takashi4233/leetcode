from typing import List
from typing import Optional

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        mid = (n)//2
        print (f"{not self.isBadVersion(mid)},{self.isBadVersion(mid+1)}")
        # whileはfalseになれば抜ける
        while self.isBadVersion(mid) == self.isBadVersion(mid+1):
            print (f"while ={mid}")
            print (f"{self.isBadVersion(mid)},{self.isBadVersion(mid+1)}")
            if self.isBadVersion(mid):
                mid = mid //2
            else:
                mid = (n + mid)//2

        return mid

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

    def isBadVersion(self,n):
        if n > 1702766719:
            return True
        return False


def main():
    s = Solution()
    input = 2126753390
    output = 1702766719
    s.test(s.firstBadVersion(input),output)

if __name__ == "__main__":
    main()


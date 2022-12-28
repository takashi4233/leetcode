from typing import List
from typing import Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 1000000000
        heigh = -1
        ans = 0
        for i in range(0,len(prices)):
            if low > prices[i]:
                low = prices[i]
                heigh=-1
		
            if heigh < prices[i]:
                heigh = prices[i]
	
            if ans < heigh-low:
                ans = heigh -low
        return ans
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = [7,1,5,3,6,4]
    output = 5
    s.test(s.maxProfit(input),output)       

    s = Solution()
    input = [7,6,5,4,3,1]
    output = 0
    s.test(s.maxProfit(input),output)       


if __name__ == "__main__":
    main()

    

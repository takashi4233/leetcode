from typing import List
class Solution:
    # (36ms/87.42%)
    # for文の書き方一つでこんなに変わる？
    def plusOne(self, digits: List[int]) -> List[int]:  
        s = "".join(map(str,digits))
        num = str(int(s) + 1)
        ans = []
        ans = [int(n) for n in num ]
        return ans
    
     #解けたけど、全体に比べて遅い（69ms / 21.23%）
    def plusOne2(self, digits: List[int]) -> List[int]:
        s = "".join(map(str,digits))
        num = str(int(s) + 1)
        ans = []
        for n in num:
            ans.append(int(n))
        return ans
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    input = [1,2,3]
    output = [1,2,4]
    s.test(s.plusOne(input),output)       
    
    input = [4,3,2,1]
    output = [4,3,2,2]
    s.test(s.plusOne(input),output)       

    input = [9]
    output = [1,0]
    s.test(s.plusOne(input),output)       
    
    

if __name__ == "__main__":
    main()

    

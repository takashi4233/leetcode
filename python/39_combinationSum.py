from typing import List
from typing import Optional

class Solution:
    #　再帰関数で解決する
    # ２分木の発送で、片方は２を使うことができるが、もう一方は２を使うことができないという条件で木を作っていく
    # 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def comb(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            comb(i,cur,total + candidates[i])
            cur.pop()
            comb(i+1,cur,total)
        comb(0,[],0)
        return res


    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    
    candidates = [2,3,6,7]
    target = 7
    output = [[2,2,3],[7]]
    ans = s.combinationSum(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

    candidates = [2,3,5]
    target = 8
    output = [[2,2,2,2],[2,3,3],[3,5]]
    ans = s.combinationSum(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

    candidates = [2]
    target = 1
    output = []
    ans = s.combinationSum(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

if __name__ == "__main__":
    main()


from typing import List
from typing import Optional

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def comb2(cur,idx,total):
            # print (f"idx = {idx}")
            # print (f"cur={cur} / total={total}")
            if total > target:
                return
            elif total == target:
                if cur not in res:
                    res.append(cur.copy())
                return
            prev = -1
            for i in range(idx,len(candidates)):
                #print (f"prev = {prev} , cand = {candidates[i]} , cand[-1] = {candidates[i-1]}")
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                comb2(cur,i + 1,total+ candidates[i])
                cur.pop()
                prev = candidates[i]

        comb2([],0,0)
        return res

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    output = [[1,1,6],[1,2,5],[1,7],[2,6]]
    ans = s.combinationSum2(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

    candidates = [2,5,2,1,2]
    target = 5
    output = [[1,2,2],[5]]
    ans = s.combinationSum2(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

    candidates = [3,1,3,5,1,1]
    target = 8
    output = [[1,1,1,5],[1,1,3,3],[3,5]]
    ans = s.combinationSum2(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 27
    output = []
    ans = s.combinationSum2(candidates,target)
    print (f"ans = {ans}")
    print (f"out = {output}")

if __name__ == "__main__":
    main()


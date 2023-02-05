from typing import List
from typing import Optional

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print (nums)
        goal = len(nums) -1
        for i in range(len(nums)-1 , -1, -1):
            print (f"goal = {goal}, i = {i}")
            if i + nums[i] >= goal:
                goal = i
        return True if goal ==0 else False
        
        
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                print (f"i = {i}")
                for j in range(i,-1,-1):
                    print(f"i={i},j={j},nums[j]={nums[j]}")
                    if nums[j] > i - j:
                        print ("break")
                        break
                if j == 0:
                    return False
        return True
        """

        """ 
        s = ",".join(map(str,nums))
        print (s)
        a = s.split("0")
        print (a)
        for  b in a:
            c = b.split(",")
            print (c)
            c = list(filter(None,c))
            print (c)
            for d in c:
                if int(d) > len(b):
                    return False
        return True

        path = [nums[0]]
        length = len(nums) -1
        while True:
            if path[-1] == 0:
                path.pop()
            #print (f"nums = {nums}")
            path.append(nums[sum(path)])
            print(f"path = {path}")
            #print (f"index = {index}, nums = {nums[index]}")
            if sum(path) >= length:
                return True
            if nums[sum(path)] == 0:
                path[-1] = path[-1] -1
                if path[-1] <= 1:
                    path.pop()
                    if len(path) == 0:
                        return False
                    path[-1] = path[-1] -1
        """
                

        """
        while index < len(nums):
            print (f"index={index},num={nums[index]},le={len(nums)}")
            if index == len(nums)-1:
                return True
            if nums[index] == 0:
                if index <= 0:
                    return False
                else:
                    index = index -1
            else:
                index = index + nums[index]
        return True
        """

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    input = [3,2,1,0,4]
    output = False
    s.test(s.canJump(input),output)

if __name__ == "__main__":
    main()


from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Noneという値が許されていることを明示されている場合は、引数がオプションであろうがなかろうと、Optionalを使うのが好ましい
class Solution:
    
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index = 0
        if m == 0:
            for i in range(0,n):
                nums1.insert(i,nums2[0])
                del(nums2[0])
                nums1.pop()
                
                #print (f"a {nums1}")
                
                
        else:
            for i in range(0,len(nums1)):
                #print (f"i = {i} / m = {m}  / mums1[{i}] = {nums1[i]},nums2[0] = {nums2[0]} / nums1 = {nums1}, num2 = {nums2}")
                #print(f"{i},{m}/{nums1[i]},{nums2[0]}")
                if len(nums2) == 0:
                    break;
                
                if i == (m+index) and nums1[i] == 0:
                    print (f"i == m == {i} and nums1[i] == 0 and nums2[0] = {nums2[0]}")
                    nums1.insert(i,nums2[0])
                    del(nums2[0])
                    nums1.pop()
                    i = i-1
                    index += 1
                
                
                elif nums1[i] < nums2[0] and (m+index) < i:
                    ##print (f"!!!!! nums1[{i}] = {nums1[i]}")
                    if nums1[i] != 0:
                        nums1.insert(i+1,nums2[0])
                    else:
                        nums1.insert(i,nums2[0])
                    del(nums2[0])
                    nums1.pop()
                    i = i-1
                    index += 1
                
                #elif nums1[i]  == nums2[0]:
                #    print (f"= nums1[i] = {nums1[i]}")
                    
                elif nums1[i] > nums2[0]:
                    #print (f"> nums1[{i}] = {nums1[i]} , nums2[0] = {nums2[0]}")
                    nums1.insert(i,nums2[0])
                    del(nums2[0])
                    nums1.pop()
                    i = i-1
                    index += 1
                    
#            if nums1[i] == 0:
#                nums1.insert(i,nums2[0])
#                del(nums2[0])
#                nums1.pop()
#                i = i-1
                
            
        
        print (f"ans = {nums1}")
        return nums1
        
        
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    
    """
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1,m,nums2,n)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1,m,nums2,n)
    
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1,m,nums2,n)
    
    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 6
    nums2 = [1,2,2]
    n = 3
    s.merge(nums1,m,nums2,n)
    
    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    s.merge(nums1,m,nums2,n)
    

    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5
    s.merge(nums1,m,nums2,n)
    
    
    nums1 = [4,0,0,0,0,0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5
    s.merge(nums1,m,nums2,n)

    nums1 = [0,2,0,0,0,0,0]
    m = 2
    nums2 = [-1,-1,2,5,6]
    n = 5
    nums1 = s.merge(nums1,m,nums2,n)
    s.test(nums1,[-1,-1,0,2,2,5,6])
    """
    nums1 = [-10,-10,-10,-10,-10,-10,-9,-9,-9,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-4,-4,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,2,3,3,3,3,3,3,4,4,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    m = 75
    nums2 = [-10,-10,-10,-8,-8,-6,-6,-6,-6,-4,-4,-4,-3,-3,-3,-3,-2,-1,1,1,1,1,2,3,4,5,5,6,6,6,8,8,8,9,9]
    n = 35
    ans = [-10,-10,-10,-10,-10,-10,-10,-10,-10,-9,-9,-9,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,3,4,4,4,5,5,5,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9]
    s.test(s.merge(nums1,m,nums2,n),ans)
    


if __name__ == "__main__":
    main()

    

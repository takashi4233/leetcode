from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 一回array形式に戻してといているので、ListNodeのまま解く方法を考えてもいいかも。
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = self.ListNode2Array(l1)
        ll2 = self.ListNode2Array(l2)
        
        # reverse()はNoneを返すので注意が必要
        ll1.reverse()
        ll2.reverse()
        
        s1 = "".join(map(str,ll1))
        s2 = "".join(map(str,ll2))
        
        i1 = int(s1)
        i2 = int(s2)
        ans = str(i1+i2)
        
        # 文字列をarraylistに変換
        ans = list(ans)
        ans.reverse()
        
        ans2 = self.setListNode(ans)
            
        return ans2
    
    
    # ArrayからListに変換    
    def setListNode(self,input) -> Optional[ListNode]:
        l_head = ListNode(0)
        l = l_head
        for i in input:
            l.next = ListNode(i)
            l = l.next
        return l_head.next
    
    # ListNodeの中身を表示
    def showListNode(self,input:Optional[ListNode]):
        while input != None:
            print (f"{input.val}",end=",")
            input = input.next
        print()
        
    # ListNodeを配列に変換
    def ListNode2Array(self,input:Optional[ListNode]) -> List[int]:
        nums = []
        while input != None:
            nums.append(input.val)
            input = input.next
        return nums
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    l1 = s.setListNode([2,4,3])
    l2 = s.setListNode([5,6,4])
    output = [7,0,8]
    s.test(s.addTwoNumbers(l1,l2),output)
    
    l1 = s.setListNode([0])
    l2 = s.setListNode([0])
    output = [0]
    s.test(s.addTwoNumbers(l1,l2),output)
    
    l1 = s.setListNode([9,9,9,9,9,9,9])
    l2 = s.setListNode([9,9,9,9])
    output = [8,9,9,9,0,0,0,1]
    s.test(s.addTwoNumbers(l1,l2,output))
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    main()

    

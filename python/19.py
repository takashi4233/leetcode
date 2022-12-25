from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Noneという値が許されていることを明示されている場合は、引数がオプションであろうがなかろうと、Optionalを使うのが好ましい
class Solution:
    
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.ListNode2Array(head)
        l.pop(len(l) - n)
        print(l)
        head = self.setListNode(l)
        return head
        
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
        print ("show:",end="")
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

    list = [1,2,3,4,5]
    p = s.setListNode(list)
    n = 2
    ans = [1,2,3,5]
    s.test(s.ListNode2Array( s.removeNthFromEnd(p,n)),ans)


    list = [1]
    p = s.setListNode(list)
    n = 1
    ans = []
    s.test(s.ListNode2Array( s.removeNthFromEnd(p,n)),ans)

    list = [1,2]
    p = s.setListNode(list)
    n = 1
    ans = [1]
    s.test(s.ListNode2Array( s.removeNthFromEnd(p,n)),ans)

if __name__ == "__main__":
    main()

    

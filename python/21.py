from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Noneという値が許されていることを明示されている場合は、引数がオプションであろうがなかろうと、Optionalを使うのが好ましい
class Solution:
    # ListNodeをArrayに変換しようと考えたけど、ListNodeのまま処理するほうが良いと方向転換
    # ListNodeの使い方がいまいちわからないので、Arrayに変換する方法を考えても良いと思う
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3_head = ListNode(0)
        list3 = l3_head
        while (list1 != None and list2 != None):
            if list1.val >= list2.val:
                list3.next = list2
                list2 = list2.next
            else:
                list3.next = list1
                list1 = list1.next
            list3 = list3.next
        if list1:
            list3.next = list1
        if list2:
            list3.next = list2

        return l3_head.next            
        
        
def main():
    s = Solution()      
    s.mergeTwoLists()

if __name__ == "__main__":
    main()

    

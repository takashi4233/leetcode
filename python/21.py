from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Noneという値が許されていることを明示されている場合は、引数がオプションであろうがなかろうと、Optionalを使うのが好ましい
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.listNode2List(list1)
        print(l1)
        l2 = self.listNode2List(list2)
        print(l2)
        
        l = l1 + l2
        l.sort()
        node = self.list2ListNode(l)
        return node
        
        
    def list2ListNode(self,list:[int]):
        node = ListNode()
        
        node.val = list[0]
        node2 = ListNode()
        node.next = node2
        
        return node
    
    
    
    
    def listNode2List(self,list:Optional[ListNode]):
        l = []
        while True:
            l.append(list.val)
            print(list.val)
            if list.next == None:
                break
            else:
                list = list.next
        
        return l
            
        
        
def main():
    s = Solution()
    list1 = [1,2,4]
    l1 = ListNode()
    l1.val = 1
    l2 = ListNode()
    l2.val = 2
    l3 = ListNode()
    l3.val=4
    l2.next = l3
    l1.next = l2
    
    list2 = [1,3,4]    
    l21 = ListNode()
    l21.val = 1
    l22 = ListNode()
    l22.val = 3
    l23 = ListNode()
    l23.val=4
    l22.next = l23
    l21.next = l22

    node = s.mergeTwoLists(l1,l2)
    print(node.val)
    return node
    
    
    
        

if __name__ == "__main__":
    main()

    

from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tmp = ListNode(next=head)
        cur = head
        prev = tmp
        
        while cur:
            next = cur.next
            if cur.val == val:
                prev.next = next
            else:
                prev = cur
            cur  = next
        return tmp.next

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    head = ListNode(1)
    c = head
    nums = [1,2,6,3,4,5,6]
    for n in nums:
        c.next = ListNode(n)
        

if __name__ == "__main__":
    main()


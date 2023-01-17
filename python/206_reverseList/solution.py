from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    head = ListNode(1)
    c = head
    nums = [2,3,4,5]
    for n in nums:
        c.next = ListNode(n)
        c = c.next
    while head:
        print (head.val)
        head = head.next

    h = s.reverseList(c)


if __name__ == "__main__":
    main()


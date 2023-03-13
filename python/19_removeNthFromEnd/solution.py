from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #        if n == 1 and head.next is None:
        #            return None
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    ary = [1, 2, 3, 4, 5]
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    n = 2
    sol.removeNthFromEnd(l, n)
    while l:
        print(l.val)
        l = l.next

    l = ListNode(1)
    n = 1
    sol.removeNthFromEnd(l, n)
    while l:
        print(l.val)
        l = l.next

    l = ListNode(1)
    l.next = ListNode(2)
    n = 1
    sol.removeNthFromEnd(l, n)
    while l:
        print(l.val)
        l = l.next

    l = ListNode(1)
    l.next = ListNode(2)
    n = 2
    sol.removeNthFromEnd(l, n)
    while l:
        print(l.val)
        l = l.next


if __name__ == "__main__":
    main()

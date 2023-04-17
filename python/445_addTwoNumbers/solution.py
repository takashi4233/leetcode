from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # list1, list2 = [], []
        res = ListNode(0)
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        print(f"l1={num1},l2={num2}")
        tmp = res
        for n in list(str(num1 + num2)):
            tmp.next = ListNode(n)
            tmp = tmp.next
        return res.next

    def test(self, input, answer):
        assert input == answer, "期待する値[{1}], 入力値[{0}]".format(input, answer)


def main():
    sol = Solution()
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    output = sol.addTwoNumbers(l1, l2)

    while output:
        print(output.val)
        output = output.next


if __name__ == "__main__":
    main()

from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 65ms (62.16%)
    # フロイトの循環検出法（うさぎとかめのアルゴリズム）
    # 余談だが、うさぎとかめは（Turtle and rabbitではなく、
    # Tortoise(陸ガメ) and Hare（野うさぎ）
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        tortoise = head
        hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            #値じゃなくてオブジェクトとして同じかで比較する
            if tortoise == hare:
                return True
        return False

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    head = ListNode(-3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next


    s = Solution()
    s.hasCycle(head)

if __name__ == "__main__":
    main()


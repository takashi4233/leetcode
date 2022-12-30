from typing import List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = head
        # Nodeごと変えようとせずに、Nodeのリンクはそのままに値だけを変更する
        while head and head.next:
            tmp = head.val
            head.val = head.next.val
            head.next.val = tmp
            head = head.next.next
        return list

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

    # ArrayからListに変換
    def setListNode(self,input) -> Optional[ListNode]:
        l_head = ListNode(0)
        l = l_head
        for i in input:
            l.next = ListNode(i)
            l = l.next
        return l_head.next

    # ListNodeを配列に変換
    def ListNode2Array(self,input:Optional[ListNode]) -> List[int]:
        nums = []
        while input != None:
            nums.append(input.val)
            input = input.next
        return nums

def main():
    s = Solution()

    list = [1,2,3,4]
    p = s.setListNode(list)
    p2 = s.swapPairs(p)
    b = s.ListNode2Array(p2)

    a = s.ListNode2Array(p)
    print (f"a={a},b={b}")
    output = [2,1,4,3]


    s.test(a,output)

if __name__ == "__main__":
    main()


from typing import Optional
from typing import List
import pytest
from solution import ListNode
import solution
@pytest.fixture
def solution_ins():
    return solution.Solution()

def listNode2Array(head)-> Optional[List]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def array2ListNode(nums) -> Optional[ListNode]:
    if len(nums) == 0:
        return

    head = ListNode(nums[0])
    c = head
    for i in range(1,len(nums)):
        c.next = ListNode(nums[i])
        c = c.next
    return head

@pytest.mark.parametrize(('arg1', 'arg2','expected'), [
    ([1,2,6,3,4,5,6],6, [1,2,3,4,5]),
    ([],1, []),
    ([7,7,7,7],7, [])
])

def test_base(solution_ins,arg1,arg2,expected):
    head = array2ListNode(arg1)
    head = solution_ins.removeElements(head,arg2)
    assert listNode2Array(head) == expected

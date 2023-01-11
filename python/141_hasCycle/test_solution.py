import pytest
import solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
@pytest.fixture
def solution_ins():
    return solution.Solution()

# @pytest.mark.parametrize(('s', 't','expected'), [
#     ("hoge","", 3),
#     ("rat","", False),
# ])

def test_base(solution_ins):
    head = ListNode(-3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert solution_ins.hasCycle(head) == True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert solution_ins.hasCycle(head) == True
    
    
    head = ListNode(1)
    assert solution_ins.hasCycle(head) == False
    
    head = None
    assert solution_ins.hasCycle(head) == False

    head = ListNode(1)
    head.next = ListNode(2)
    assert solution_ins.hasCycle(head) == False


from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Noneという値が許されていることを明示されている場合は、引数がオプションであろうがなかろうと、Optionalを使うのが好ましい
class Solution:
    
    
    # Acceptだけど、遅い（105ms / 6.33%）
    # print文をコメントアウトしたら（ 55ms / 73.3%）になった。
    # 本番のコードはprint文を削除するように注意しよう。
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(-101)
        pre = pre_head
        while head != None:
            #print(f"pre={pre.val},input.val={head.val}")
            if pre.val != head.val:
            #    print(f"linked:{head.val}")
                pre.next = ListNode(head.val)
                pre = pre.next
            head = head.next
        return pre_head.next
        
        
    # ArrayからListに変換    
    def setListNode(self,input) -> Optional[ListNode]:
        l_head = ListNode(0)
        l = l_head
        for i in input:
            l.next = ListNode(i)
            l = l.next
        return l_head.next
    
    # ListNodeの中身を表示
    def showListNode(self,input:Optional[ListNode]):
        print ("show:",end="")
        while input != None:
            print (f"{input.val}",end=",")
            input = input.next
        print()
        
    # ListNodeを配列に変換
    def ListNode2Array(self,input:Optional[ListNode]) -> List[int]:
        nums = []
        while input != None:
            nums.append(input.val)
            input = input.next
        return nums
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
         
        
def main():
    s = Solution()
    p = s.setListNode([1,1,2])
    ans = s.deleteDuplicates(p)
    print (f"ans.val = {ans.val}")
    s.showListNode(ans)


    p = s.setListNode([1,1,2,3,3])
    ans = s.deleteDuplicates(p)
    print (f"ans.val = {ans.val}")
    s.showListNode(ans)

if __name__ == "__main__":
    main()

    

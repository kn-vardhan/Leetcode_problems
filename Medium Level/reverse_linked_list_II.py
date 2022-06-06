# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        _list = []
        while head is not None:
            _list.append(head.val)
            head = head.next
        
        left -= 1
        right -= 1
        values = []
        for i in range(left):
            values.append(_list[i])
        for i in range(right, left-1, -1):
            values.append(_list[i])
        for i in range(right+1, len(_list)):
            values.append(_list[i])

        values = values[::-1]
        
        answer = ListNode(0)
        temp = answer
        while len(values) != 0:
            temp.next = ListNode(values.pop())
            temp = temp.next
            
        return answer.next




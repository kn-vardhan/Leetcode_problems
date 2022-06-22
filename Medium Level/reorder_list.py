# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        values = []
        temp = head
        while temp != None:
            values.append(temp.val)
            temp = temp.next
        
        answer = []
        for i in range(ceil(len(values)/2)):
            answer.append(values[i])
            answer.append(values[len(values) - i - 1])
        
        answer = answer[::-1]
        _head = ListNode(0)
        temp = _head
        while len(answer) != 0:
            temp.next = ListNode(answer.pop())
            temp = temp.next
            
        _head = _head.next
        
        while head != None and _head != None:
            head.val = _head.val
            head = head.next
            _head = _head.next



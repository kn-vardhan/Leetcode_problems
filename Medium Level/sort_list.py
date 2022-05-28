# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        
        values.sort()
        values = values[::-1]
        
        answer = ListNode(0)
        temp = answer
        while len(values) != 0:
            temp.next = ListNode(values.pop())
            temp = temp.next
            
        return answer.next

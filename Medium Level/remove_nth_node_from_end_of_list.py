# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        N = n-1
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        
        values = values[::-1]
        values.pop(N)
        
        answer = ListNode(0)
        temp = answer
        while len(values) != 0:
            temp.next = ListNode(values.pop())
            temp = temp.next
            
        return answer.next

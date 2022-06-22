# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
        
        value.sort(reverse=True)
        
        answer = ListNode(0)
        temp = answer
        while len(value) != 0:
            temp.next = ListNode(value.pop())
            temp = temp.next
            
        return answer.next



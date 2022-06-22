# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        
        count = Counter(values)
        for i in count:
            if count[i] > 1:
                while count[i] > 0:
                    values.remove(i)
                    count[i] -= 1
        
        values = values[::-1]
        answer = ListNode(0)
        temp = answer
        while len(values) != 0:
            temp.next = ListNode(values.pop())
            temp = temp.next
            
        return answer.next
    

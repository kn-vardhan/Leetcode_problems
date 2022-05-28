# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []
        while head != None:
            values.append(head.val)
            head = head.next

        N = len(values)
        if N % 2 == 0:
            for i in range(0, N, 2):
                temp = values[i+1]
                values[i+1] = values[i]
                values[i] = temp
        else:
            last = values[-1]
            values = values[:-1]
            for i in range(0, N-1, 2):
                temp = values[i+1]
                values[i+1] = values[i]
                values[i] = temp
            values.append(last)

        values = values[::-1]
        answer = ListNode(0)
        temp = answer
        while len(values) != 0:
            temp.next = ListNode(values.pop())
            temp = temp.next
            
        return answer.next

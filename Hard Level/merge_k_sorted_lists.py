# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        N = len(lists)
        final = []
        
        for l in lists:
            temp = []
            while l != None:
                temp.append(l.val)
                l = l.next
            for t in temp:
                final.append(t)
        
        final.sort(reverse=True)

        answer = ListNode(0)
        temp = answer
        while len(final) != 0:
            temp.next = ListNode(final.pop())
            temp = temp.next
            
        return answer.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while l1.next != None:
            list1.append(l1.val)
            l1 = l1.next
        while l2.next != None:
            list2.append(l2.val)
            l2 = l2.next

        list1.append(l1.val)
        list2.append(l2.val)
        list1 = list1[::-1]
        list2 = list2[::-1]
        num1 = int(''.join([str(x) for x in list1]))
        num2 = int(''.join([str(x) for x in list2]))
        
        value = num1 + num2
        value = list(map(int, str(value)))
    
        answer = ListNode(0)
        temp = answer
        while len(value) != 0:
            temp.next = ListNode(value.pop())
            temp = temp.next
            
        return answer.next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import collections
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        
        answer = []
        while queue:
            # print(queue)
            H = len(queue)
            temp_max = float("-inf")
            for i in range(H):
                node = queue.popleft()
                temp_max = max(temp_max, node.val)
            
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                
            answer.append(temp_max)
        
        return answer


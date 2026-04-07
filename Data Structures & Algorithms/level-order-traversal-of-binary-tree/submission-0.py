# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root:
            queue.append(root)
        else: 
            return []
        result = []
        while queue:
            qlen = len(queue)
            lst = []
            for i in range(qlen):
                res = queue.pop(0)
                lst.append(res.val)
                if res.left:
                    queue.append(res.left)
                if res.right:
                    queue.append(res.right)
            result.append(lst)
        return result



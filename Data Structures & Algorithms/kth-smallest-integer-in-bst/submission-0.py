# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            if root: 
                lst.append(root.val)
            if root.right: 
                dfs(root.right)
        dfs(root)
        return lst[k-1]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def compare(root, lb, ub):
            if root: 
                if lb< root.val < ub:
                    return compare(root.left, lb, root.val) and compare(root.right, root.val, ub)
                else: 
                    return False
            return True

        return compare(root, -1001, 1001)
        
                


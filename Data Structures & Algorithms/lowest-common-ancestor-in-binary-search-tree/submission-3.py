# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val = root.val
        pval = p.val
        qval = q.val

        if val == pval: 
            return root
        if val == qval :
            return root

        if pval < val < qval or qval < val < pval: 
            return root
        if val < p.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return self.lowestCommonAncestor(root.left, p, q)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def treeToString(self, root):
        if root == None: 
            return "*"
        return str(root.val) + self.treeToString(root.left) + self.treeToString(root.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = self.treeToString(root)
        sub = self.treeToString(subRoot)
        print(tree, sub)
        if sub in tree:
            return True
        else:
            return False
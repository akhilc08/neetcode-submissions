# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return None

        if key < root.val: 
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)

        else: 
            successor = None
            if root.right: 
                successor = root.right
                while successor.left: 
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
            elif root.left: 
                successor = root.left 
                while successor.right: 
                    successor = successor.right
                root.val = successor.val
                root.left = self.deleteNode(root.left, successor.val)
            else: 
                root = None
        return root


        
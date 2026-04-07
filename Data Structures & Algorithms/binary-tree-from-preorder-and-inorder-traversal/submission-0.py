# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        
        root = TreeNode(preorder[0])

        lotree = inorder[:inorder.index(root.val)]
        rotree = inorder[inorder.index(root.val)+1:]
        lptree = preorder[1:1+len(lotree)]
        rptree = preorder[1+len(lotree):]

        root.left = self.buildTree(lptree, lotree)

        root.right = self.buildTree(rptree, rotree)


        return root

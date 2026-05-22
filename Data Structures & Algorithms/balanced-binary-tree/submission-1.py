# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanced(self, root, heights): 
        if not root: return True

        if not root.left and not root.right: 
            heights[root] = 1
            return True
        elif not root.left:
            balanced = self.balanced(root.right,heights)
            heights[root] = heights[root.right]+1
            return True if heights[root.right] == 1 and balanced else False

        elif not root.right: 
            balanced = self.balanced(root.left,heights)
            heights[root] = heights[root.left]+1
            return True if heights[root.left] == 1 and balanced else False

        else:
            l_balanced = self.balanced(root.left,heights)
            r_balanced = self.balanced(root.right,heights)

            heights[root] = max(heights[root.left], heights[root.right]) + 1

            return True if l_balanced and r_balanced and abs(heights[root.left] - heights[root.right]) <2 else False



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root, {})

        


        
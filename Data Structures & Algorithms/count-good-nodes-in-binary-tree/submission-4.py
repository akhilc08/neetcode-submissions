# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m, counter): 
            if not node.left and not node.right: 

                if node.val < m: 

                    return counter
                else:

                    return counter+1
            elif not node.left: 
                if node.val < m: 

                    return dfs(node.right,m, counter)
                else: 
                    return dfs(node.right,node.val,counter+1)
            elif not node.right: 

                if node.val <m: 
                    
                    return dfs(node.left, m, counter)
                else: 
                    return dfs(node.left,node.val, counter+1)
            else:

                if node.val < m:
                    return dfs(node.left, m, counter) + dfs(node.right, m, 0)
                else:
                    return dfs(node.left, node.val, counter+1) + dfs(node.right, node.val, 0)
        
        return dfs(root,root.val, 0)
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        hmap = {}

        def dfs(node): 
            if not node: return 0

            l, r = 0,0
            if node in hmap: 
                return hmap[node]

            if node.left and node.right: 
                l = dfs(node.left.left) + dfs(node.left.right)
                r = dfs(node.right.left) + dfs(node.right.right)

                hmap[node] = max(dfs(node.left) + dfs(node.right), node.val + l+r)
                return hmap[node]

            elif node.left: 
                l = dfs(node.left.left) + dfs(node.left.right)
                hmap[node] = max(dfs(node.left), node.val+l)
                return hmap[node]

            
            elif node.right: 
                r = dfs(node.right.left) + dfs(node.right.right)
                hmap[node] = max(dfs(node.right), node.val+r)
                return hmap[node]

            else: 
                hmap[node] = node.val
                return node.val

        return dfs(root)
        
        
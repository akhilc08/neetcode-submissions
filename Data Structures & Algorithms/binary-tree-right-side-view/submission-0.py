# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []

        def bfs(root): 

            queue = collections.deque()
            queue.append((0, 0, root))
            level = 0
            horizontal = 0
            while queue: 
                popped = queue.popleft()
                node = popped[2]
                if not node: 
                    continue
                
                else: 
                    result.append(popped)
                    new_level = popped[0]
                    if level != new_level: 
                        level = new_level 
                        horizontal = 0
                    

                    queue.append((popped[0]+1, horizontal,node.left))
                    horizontal += 1
                    queue.append((popped[0]+1, horizontal,node.right))
                    horizontal += 1
        if root: bfs(root) 
        else: return []
        print(result)
        res = []
        for i in range(1,len(result)): 
            if result[i][0] != result[i-1][0]: 
                res.append(result[i-1][2].val)
        res.append(result[len(result)-1][2].val)
        return res

        
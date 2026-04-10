"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        
        result = Node(node.val)
        visited = {node:result}

        def dfs(root, root_copy):
            for child in root.neighbors: 
                if child not in visited: 
                    neighbor = Node(child.val)
                    visited[child] = neighbor
                    root_copy.neighbors.append(neighbor)
                    dfs(child, neighbor)
                else: 
                    neighbor = visited[child]
                    root_copy.neighbors.append(neighbor)
        dfs(node, result)
        return result




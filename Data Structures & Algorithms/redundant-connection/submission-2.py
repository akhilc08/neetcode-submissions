class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [0]*(len(edges)+1)
        for i in range(len(edges)+1): 
            parent[i] = i
        
        rank = [1] * (len(edges)+1)

        def union(n1,n2): 
            p1,p2 = find(n1),find(n2)
            if p1 == p2: 
                return False

            if rank[p1] > rank[p2]: 

                parent[p2] = p1
                rank[p1]+=rank[p2]
            
            else: 
                parent[p1] = p2
                rank[p2]+=rank[p1]
            
            return True

        def find(n1): 
            if n1 == parent[n1]: 
                return n1
            return find(parent[n1])

        for edge in edges: 
            n1,n2 = edge
            if union(n1,n2) == False: 
                return edge


        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        aj = defaultdict(list)
        for n1, n2 in edges: 
            aj[n1].append(n2)
            aj[n2].append(n1)

        visited = set()
        def dfs(node): 
            visited.add(node)
            con = aj[node]
            for c in con: 
                if c not in visited: 
                    visited.add(c)
                    dfs(c)


        res = 0
        for i in range(n): 
            if i not in visited: 
                res +=1
                dfs(i)

        return res

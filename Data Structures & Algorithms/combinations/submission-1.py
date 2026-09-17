class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        def dfs(start,curr,k):
            for i in range(start,n+1):
                if len(curr)+1 == k: 
                    result.append(curr+[i])
                else:
                    dfs(i+1,curr+[i],k)
            


        dfs(1,[],k)            
        return result

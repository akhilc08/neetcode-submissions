class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        sets = []
        res = []

        def back(start): 
            if len(res) == k: 
                sets.append(res.copy())
                return 
            if start > n: return 
            
            for i in range(start, n+1): 
                res.append(i)

                back(i+1)

                res.remove(i)
        
        back(1)
        return sets 

        
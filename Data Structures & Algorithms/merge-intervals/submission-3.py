class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        
        for s2, e2 in intervals: 
            if not res: 
                res.append([s2,e2])
            else: 
                s1, e1 = res[-1]
                if e1 >= s2: 
                    res.pop()
                    res.append([min(s1, s2), max(e1, e2)])
                else: 
                    res.append([s2,e2])

        return res 
 

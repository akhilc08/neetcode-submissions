class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusted = defaultdict(list)
        trusts = defaultdict(list)

        for p1, p2 in trust: 
            trusts[p1].append(p2)
            trusted[p2].append(p1)

        print(trusts)
        print(trusted)

        for i in range(1,n+1): 
            if not trusts[i]: 

                if len(trusted[i]) == n-1:
                    return i
        
        return -1

        
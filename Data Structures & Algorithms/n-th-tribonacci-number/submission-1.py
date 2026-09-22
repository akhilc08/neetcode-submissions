class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0]*n
        if n == 0: return 0
        if n == 1 or n==2: return 1
        for i in range(n): 
            if i== 0: 
                t[i] = 0
            elif i<3: 
                t[i] = 1
            else: 
                t[i] = t[i-1]+t[i-2]+t[i-3]
        
        return t[n-1]+t[n-2]+t[n-3]

class Solution:
    def trap(self, height: List[int]) -> int:

        
        maxl = height[0]
        maxr = height[len(height)-1]

        l, r = 1, len(height)-2


        res = 0


        while l<=r: 
            if maxl < maxr: 
                water = maxl - height[l]
                res += water if water > 0 else 0
                maxl = max(maxl, height[l])
                l+=1
            else: 
                water = maxr - height[r]
                res += water if water > 0 else 0
                maxr = max(maxr, height[r])
                r-=1

        return res 

        
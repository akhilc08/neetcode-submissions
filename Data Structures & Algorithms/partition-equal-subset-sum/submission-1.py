class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0: return False

        nums.sort(reverse=True)

        hmap = {}

        def dfs(start, p1, p2): 
            if (start,p1,p2) in hmap: return hmap[(start,p1,p2)]

            if start == len(nums): 
                return p1 == p2
            
            
            if nums[start] <= p1: 
                p1 -= nums[start]
                hmap[(start,p1,p2)] = dfs(start+1,p1,p2)
                

                if hmap[(start,p1,p2)]: return True 
                p1 += nums[start]

            if nums[start] <= p2: 
                p2 -= nums[start]
                hmap[(start,p1,p2)] = dfs(start+1,p1,p2)
                

                if hmap[(start,p1,p2)]: return True
                p2 += nums[start] 
            
            return False 
        
        return dfs(0, total//2, total//2)
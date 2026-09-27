class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0: return False
        
        parts = [total//2] * 2 

        nums.sort(reverse=True)

        hmap = {}

        def dfs(start): 
            if start in hmap: return hmap[start]

            if start == len(nums): 
                return parts[0] == parts[1]
            
            for i in range(2): 
                if nums[start] <= parts[i]: 
                    parts[i] -= nums[start]
                    hmap[start] = dfs(start+1)

                    if hmap[start]: return True 

                    parts[i] += nums[start]
            
            return False 
        
        return dfs(0)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        hmap = {}

        def dfs(start): 
            if start in hmap: return hmap[start]
            long = 0
            for i in range(start,len(nums)): 
                if nums[i] > nums[start]: 
                    long = max(dfs(i), long)
                
            hmap[start] = 1+long
            return hmap[start]
        
        longest = 0
        for i in range(len(nums)): 
            longest = max(longest, dfs(i))

        return longest
        
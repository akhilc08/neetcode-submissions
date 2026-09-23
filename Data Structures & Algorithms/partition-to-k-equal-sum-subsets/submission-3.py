class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums) % k != 0: return False

        sums = sum(nums)//k

        parts = [sums]*k

        nums.sort(reverse=True)

        def dfs(start): 
            if start == len(nums): 
                return True

            seen = set()
            for i in range(k): 
                if parts[i] < nums[start] or parts[i] in seen: 
                    continue
                seen.add(parts[i])
                parts[i] -= nums[start]
                if dfs(start+1): return True
                parts[i] += nums[start]

            return False
        
        return dfs(0)


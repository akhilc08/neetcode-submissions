class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums) 
        if total%k != 0: return False

        parts = [total//k]*k
        nums.sort(reverse=True)

        def back(start): 

            if start == len(nums) and (nums[i] == 0 for i in range(k)): 
                return True


            visited = set()
            for i in range(k): 
                if parts[i] - nums[start] >= 0 and parts[i] not in visited: 
                    visited.add(parts[i])
                    parts[i] -= nums[start]

                    if back(start+1): return True

                    parts[i] += nums[start]
            
            return False

        return back(0)
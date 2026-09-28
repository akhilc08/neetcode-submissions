class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i = 0
        total = 0
        res = math.inf

        for j in range(len(nums)): 
            total += nums[j]
            if total>=target: 
                while total >= target: 
                    res = min(res, j-i+1)
                    total -= nums[i]
                    i+=1

        return res if res != math.inf else 0
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cache = {}

        def canJumpHelp(i): 
            if i in cache: return cache[i]
            if i >= len(nums)-1: return True

            can = False
            for j in range(1,nums[i]+1): 
                if canJumpHelp(i+j): 
                    can = True
            cache[i] = can
            return can

        return canJumpHelp(0)

                

        


        
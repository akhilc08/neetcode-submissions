class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 1 2 8
        # 48 24 6 1

        # 48 24 12 8

        pref = [1]* len(nums)
        suff = [1] * len(nums)
        res = []

        for i in range(1,len(nums)): 
            pref[i] = pref[i-1]* nums[i-1]
            suff[len(nums)-1-i] = suff[len(nums)-i] * nums[len(nums)-i]


        for i in range(len(nums)): 
            res.append(pref[i]*suff[i])

        return res

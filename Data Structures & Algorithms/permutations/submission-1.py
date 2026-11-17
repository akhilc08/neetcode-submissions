class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1: 
            return [nums]

        permutations = self.permute(nums[1:])
        num = nums[0]

        res = []
        for perm in permutations: 
            for i in range(len(perm)+1): 
                pcopy = perm.copy()
                pcopy.insert(i,num)
                res.append(pcopy)

        return res 
         
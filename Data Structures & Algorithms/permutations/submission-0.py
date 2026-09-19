class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: 
            return [nums]
        
        perms = self.permute(nums[1:])
        num = nums[0]
        print(num,perms)

        res = []
        for perm in perms: 
            for i in range(len(perm)+1): 
                p_copy = perm.copy()
                p_copy.insert(i,num)
                res.append(p_copy)

        print (res)
        
        return res


        
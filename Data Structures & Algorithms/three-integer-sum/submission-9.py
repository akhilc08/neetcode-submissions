class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()


        res = set()

        for i in range(len(nums)): 
            j = i+1 
            k = len(nums)-1 

            while j<k: 
                if nums[i] + nums[j] + nums[k] == 0: 
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                if nums[i] + nums[j] + nums[k] < 0: 
                    j += 1
                if nums[i] + nums[j] + nums[k] > 0: 
                    k -= 1
        
        ret = []
        for item in res: 
            ret.append(list(item))

        return ret
            






        
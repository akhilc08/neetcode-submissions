class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)): 
            j = i+1 
            k = len(nums)-1
            target = 0-nums[i]

            while j<k: 
                if nums[j] + nums[k] == target: 
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                if nums[j] + nums[k] > target: 
                    k-=1
                if nums[j] + nums[k] < target: 
                    j+=1
        
        result = []
        for item in res: 
            result.append(list(item))
        return result
                






        
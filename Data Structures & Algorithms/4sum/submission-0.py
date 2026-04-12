class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        if len(nums)<4: 
            return result

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                new_target = target - nums[i] - nums[j]
                l = j+1
                r = len(nums)-1
                while l<r: 
                    if nums[l] + nums[r] == new_target:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -=1
                    elif nums[l] + nums[r] < new_target:
                        l+=1
                    elif nums[l] + nums[r] > new_target:
                        r-=1
        return result
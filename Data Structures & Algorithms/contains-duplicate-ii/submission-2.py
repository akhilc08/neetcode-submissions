class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False

        i,j = 0,1

        while j < len(nums): 
            if (j-i) >k: 
                i+=1
                j = i+1
            else: 
                if nums[i] == nums[j]: 
                    return True
                
                j+=1
                if j == len(nums): 
                    i+=1
                    j = i+1
        
        return False



        
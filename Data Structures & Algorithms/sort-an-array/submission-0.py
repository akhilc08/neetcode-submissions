class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) > 1: 
            larr = nums[:len(nums)//2]
            rarr = nums[len(nums)//2:]

            larr = self.sortArray(larr)
            rarr = self.sortArray(rarr)

            i = j = k = 0


            while i < len(larr) and j < len(rarr): 
                
                if larr[i] < rarr[j]: 
                    nums[k] = larr[i]
                    i+=1
                else: 
                    nums[k] = rarr[j]
                    j+=1

                k+=1

            while i<len(larr): 
                nums[k] = larr[i]
                i+=1
                k+=1
            
            while j < len(rarr):
                nums[k] = rarr[j]
                j+=1
                k+=1

        return nums
            


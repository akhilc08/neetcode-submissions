class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0: return None
        
        new = []
        k %= len(nums)
        l = len(nums)-k
        n = 0
        for i in range(len(nums)):
            if l>len(nums)-1 or l<0: 
                l = 0
            new.append(nums[l])
            l+=1
        print(new)
        nums[:] = new
        return None
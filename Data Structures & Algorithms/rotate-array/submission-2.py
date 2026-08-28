class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == 0: 
            return None
        if k > len(nums): 
            k %= len(nums)

        newlist = []
        while k > 0: 
            newlist.append(nums.pop(len(nums)-k))
            k-=1
        nums[:] = newlist+nums

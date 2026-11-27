class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(l, r): 
            if l > r: 
                return -1

            if l == r: 
                if nums[l] == target: 
                    return l
                else: return -1

            m = (r+l)//2

            if nums[m] == target: 
                return m 
            if nums[m] < target: 
                return bsearch(m+1,r)
            if nums[m] > target: 
                return bsearch(l,m-1)
            
        return bsearch(0, len(nums)-1)

        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst_search(l,r,lst,target):

            if l>r: 
                return -1
            elif r-l == 1: 
                if lst[l] == target: 
                    return l
                if lst[r] == target: 
                    return r
                return -1

            m = int (l+((r-l) / 2))
            print(m)
            if lst[m] == target: return m
            elif lst[m] < target: 
                return bst_search(m+1,r,lst,target)
            else: 
                return bst_search(l,m-1,lst,target)
        return bst_search(0,len(nums)-1,nums,target)
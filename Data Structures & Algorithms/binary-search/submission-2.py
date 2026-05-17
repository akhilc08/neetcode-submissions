class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst_search(l,r,lst,target):
            if l == r or l>r: 
                return l if lst[l] == target else -1
            elif r-l == 1: 
                if lst[l] == target: return l
                if lst[r] == target: return r
                return -1
            else:
                mid = int((r+l)/2)
                if target>lst[mid]:
                    return bst_search(mid,r,lst,target)
                else: 
                    return bst_search(l,mid,lst,target)
            
        return bst_search(0,len(nums)-1,nums,target)



        
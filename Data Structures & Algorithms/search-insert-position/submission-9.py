class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bst(l,r,lst,target):
            print(l,r,((l+r)//2))

            if l>r: 
                if r == -1: return 0
                if l-r ==1: 
                    if target == lst[r]: return r
                    if target == lst[l]: return l 
                    if lst[r]<target and target<lst[l]: return r+1
                    if lst[r]>target: return r
                    if lst[l]<target: return l+1
                    

            if l==r:
                if lst[l] == target: return l
                elif lst[l] < target: return l+1
                else: return l
            
            m = ((l+r)//2)
            if lst[m] == target: return m
            if lst[m] < target: return bst(m+1,r,lst,target)
            else: return bst(l,m-1,lst,target)

        return bst(0,len(nums)-1,nums,target)
        
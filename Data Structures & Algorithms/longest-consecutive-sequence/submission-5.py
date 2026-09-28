class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        found = set()
        for num in nums: 
            found.add(num)

        res = 1
        for num in nums: 
            curr = 1
            if num-1 not in found: 
                i = 1
                while num+i in found: 
                    curr+=1
                    i+=1
                res = max(curr,res)
        
        return res
        
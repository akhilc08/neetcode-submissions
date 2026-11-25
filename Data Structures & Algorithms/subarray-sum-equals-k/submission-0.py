class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        curr = 0
        hmap = defaultdict(int)
        hmap[0] = 1 
        res = 0

        for num in nums: 
            curr += num
            diff = curr-k
            res+= hmap[diff]
            hmap[curr] += 1
        return res
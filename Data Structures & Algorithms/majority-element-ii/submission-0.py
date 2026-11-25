class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hmap = defaultdict(int)

        for num in nums: 
            hmap[num] +=1 

        res = []
        for k,v in hmap.items(): 
            if v > len(nums)//3: 
                res.append(k)

        return res
        
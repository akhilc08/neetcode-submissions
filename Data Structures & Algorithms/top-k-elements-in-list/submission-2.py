class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1+count.get(num,0)

        for key,v in count.items(): 
            res[v].append(key)

        ret = []
        for i in range(len(res)-1, 0, -1): 
            for num in res[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret

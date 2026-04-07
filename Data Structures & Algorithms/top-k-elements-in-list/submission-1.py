class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums: 
            map[num] = 1 + map.get(num, 0)

        nums = []
        heapq.heapify(nums)
        for key,value in map.items():
            heapq.heappush(nums, (value,key))
            if len(nums) > k:
                heapq.heappop(nums)
        
        result = []
        for pair in nums: 
            result.append(pair[1])
        return result
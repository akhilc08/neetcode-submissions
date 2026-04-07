class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        if not nums:
            return 0
        for num in nums:
            map[num] = 1
        
        longest = 1
        for num in nums: 
            current = 1
            prev = num-1
            if prev not in map:
                i=1
                while num+i in map:
                    current += 1
                    i+=1
            if current > longest:
                longest = current
        return longest

        
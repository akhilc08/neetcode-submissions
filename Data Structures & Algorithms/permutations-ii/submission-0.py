class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        num_map = defaultdict(int)

        for num in nums: 
            num_map[num]+=1

        res = []
        curr = []
        
        def dfs():
            if len(curr) == len(nums): 
                res.append(curr.copy())
                return

            for k in num_map: 
                if num_map[k] > 0: 
                    curr.append(k)
                    num_map[k] -=1
                    dfs()
                    num_map[k]+=1
                    curr.pop()
        
        dfs()
        return res




        
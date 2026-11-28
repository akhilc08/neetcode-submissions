class Solution:
    def jump(self, nums: List[int]) -> int:

        goal = len(nums)-1

        jumps = 0
        while goal != 0: 
            for i in range(0,goal): 
                if i + nums[i] >= goal: 
                    print(goal,i)
                    goal = i
                    jumps += 1
                    break
        
            
        return jumps
        
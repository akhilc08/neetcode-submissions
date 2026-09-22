class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks)%4 != 0: return False
        
        length = sum(matchsticks)//4
        sides = [0]*4
        matchsticks.sort(reverse=True)

        def dfs(start):


            if start == len(matchsticks): 
                return sides[0] == sides[1] == sides[2] == sides[3] == length

            for i in range(len(sides)): 
                if (sides[i]+matchsticks[start])<= length: 

                    sides[i]+=matchsticks[start]
                    if dfs(start+1): return True
                    sides[i]-=matchsticks[start]

            return False
        
        return dfs(0)


                
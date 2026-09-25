class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pmap = {}
        for i in range(len(position)): 
            pmap[position[i]] = speed[i]
        
        position.sort()
        fleets = 0
        prev = -1

        for i in range(len(position)-1, -1, -1): 
            
            left = target-position[i]
            finished = left/pmap[position[i]]


            if prev == -1: 
                prev = finished
                fleets +=1 
            else: 
                if finished > prev: 
                    fleets += 1
                    prev = finished
        
        return fleets

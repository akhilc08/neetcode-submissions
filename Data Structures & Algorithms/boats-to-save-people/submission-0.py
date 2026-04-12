class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 1
        boat = 0
        l = 0
        r = len(people)-1
        while not l>r:
            if boat + people[r] > limit or boat+people[l] > limit: 
                boats+=1
                boat = 0
            if boat + people[r] <= limit: 
                boat += people[r]
                r-=1
            if boat + people[l] <= limit:
                boat += people[l]
                l+=1
        
        return boats
            


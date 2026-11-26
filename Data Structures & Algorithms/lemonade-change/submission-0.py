class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = [0]*3

        for bill in bills: 
            if bill == 5:
                change[0]+=1
                continue
            if bill == 10: 
                if change[0] == 0: 
                    return False
                else: 
                    change[0] -= 1
                    change[1] += 1
            if bill == 20: 
                remaining = 15
                if change[1] > 0: 
                    remaining -= 10
                    change[1] -= 1
                
                while change[0] > 0 and remaining > 0:
                    change[0] -= 1
                    remaining -= 5

                if remaining != 0: 
                    return False
                change[2] += 1
        return True 

        
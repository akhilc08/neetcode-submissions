class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) < 2: return len(fruits)

        l = 0
        r = 2
        t1 = fruits[0]
        t2 = fruits[1] if fruits[0] != fruits[1] else None
        c1 = 1 if t2 is not None else 2
        c2 = 1 if t2 is not None else 0
        res = 2


        while l <= r and r<len(fruits): 

            t = fruits[r]

            if t1 is None and t2 is None: 
                t1 = t
                c1 += 1
            
            elif t1 is None:
                if t == t2: 
                    c2+=1
                else: 
                    t1 = t
                    c1+=1

            elif t2 is None: 
                if t == t1: 
                    c1+=1
                else: 
                    t2 = t
                    c2+=1
            elif t1 is not None and t2 is not None: 

                if t == t1: 
                    c1+=1
                elif t == t2: 
                    c2+=1
                else: 
                    while c1 > 0 and c2 > 0: 
                        tremove = fruits[l]
                        if tremove == t1: 
                            c1 -= 1
                        elif tremove == t2: 
                            c2 -= 1
                        
                        l+=1
                    
                    if c1 == 0: 
                        t1 = t
                        c1 +=1
                    elif c2 == 0: 
                        t2 = t
                        c2 += 1
            
            res = max(res, r-l+1)
            r+=1
        
        return res
        
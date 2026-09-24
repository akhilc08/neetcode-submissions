class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1: 
            return True

        hmap = {}
        for i,c in enumerate(order): 
            hmap[c] = i
        

        for i in range(1,len(words)): 
            w1, w2 = words[i-1], words[i]
            
            for j in range(len(w1)): 
                if j==len(w2): 
                    return False
                if w2[j] != w1[j]: 
                    if hmap[w1[j]] > hmap[w2[j]]: 
                        return False
                    else: 
                        break
            
        return True

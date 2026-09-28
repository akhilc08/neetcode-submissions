class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        valid = []
        for word in words: 
            if word[0] in "aeiou" and word[-1] in "aeiou": 
                valid.append(True)
            else: 
                valid.append(False)

        res = [0]*len(queries)
        for i,(l,r) in enumerate(queries): 
            l,r = (l,r)
            while l<=r: 
                if valid[l]: res[i]+=1
                l+=1
        
        return res
        
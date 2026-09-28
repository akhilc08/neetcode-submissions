class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for word in strs: 
            key = [0]*26
            for c in word: 
                key[ord(c) - ord('a')] += 1
            
            hmap[tuple(key)].append(word)

        res = []
        for k,v in hmap.items(): 
            res.append(v)
        
        return res
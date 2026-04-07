class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs: 
            strmap = [0]*26
            for char in str: 
                strmap[ord(char) - 97] += 1
            if(tuple(strmap)) in map:
                map[tuple(strmap)].append(str)
            else: 
                map[tuple(strmap)] = [str]
        
        result = []
        for v in map.values():
            result.append(v)
        return result
            

            
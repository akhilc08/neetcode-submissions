class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            words = {}
            for word in strs: 
                letters = [0]*26
                for char in word: 
                    letters[ord(char) - ord('a')] +=1
                
                key = tuple(letters)
                words.setdefault(key, []).append(word)

            result = []
            for k,v in words.items():
                result.append(v)

            return result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        results = []
        if digits == "": return results
        
        def dfs(start, curr):
            if len(curr) == len(digits):
                results.append(curr)
                return
            
            for i in range(start,len(digits)): 
                chars = phone[digits[i]]
                for c in chars: 
                    dfs(i+1,curr+c)
            
        dfs(0,"")
        return results
                    
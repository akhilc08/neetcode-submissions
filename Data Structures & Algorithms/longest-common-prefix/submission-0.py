class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i,c in enumerate(strs[0]):
            print(i)

            for word in strs[1:]: 

                if word[0:i+1] != (ans+c):

                    return ans
            ans+=c
        return ans
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        temp = ""

        l = 0
        r = len(s)-1

        while not l>r:
            temp = s[l] 
            s[l] = s[r]
            s[r] = temp

            l+=1
            r-=1

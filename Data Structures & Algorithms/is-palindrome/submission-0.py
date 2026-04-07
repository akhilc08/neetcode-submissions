class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for c in s: 
            if c.isalnum():
                clean_s += c.lower()
        print (clean_s)
        x = 0 
        y = len(clean_s) -1
        while(x<y):

            if(clean_s[x] != clean_s[y]):
                return False
            x+=1
            y-=1
        return True
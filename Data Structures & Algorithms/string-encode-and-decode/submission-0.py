class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs: 
            encoded_string+=(str(len(string))+"#"+string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while (i<(len(s))):
            length = ""
            while s[i]!="#":
                length+=s[i]
                i+=1
            i+=1
            strs.append(s[i:i+int(length)])
            i+=int(length)
        return strs



class Solution:
    def calPoints(self, operations: List[str]) -> int:

        scores = []

        for op in operations: 
            if op == "C": 
                scores.pop()
            elif op == "+":
                s1 = scores.pop()
                s2 = scores.pop()
                s3 = s1+s2

                scores += [s2,s1,s3]
            
            elif op == "D": 
                s1 = scores.pop()
                scores.append(s1)
                scores.append(s1*2)
            
            else: 
                scores.append(int(op))
            
        
        return sum(scores)
        
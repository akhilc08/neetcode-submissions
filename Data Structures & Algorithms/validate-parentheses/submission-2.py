class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s: 
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                o_char = stack.pop()
                match o_char:
                    case '(':
                        if char != ')':
                            return False
                    case '[':
                        if char != ']':
                            return False
                    case '{':
                        if char != '}':
                            return False
        
        return len(stack) == 0
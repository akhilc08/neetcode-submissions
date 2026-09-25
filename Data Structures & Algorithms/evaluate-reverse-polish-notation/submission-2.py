class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens: 
            if token == "+": 
                stack.append(stack.pop() + stack.pop())
            elif token == "/": 
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(float(n1)/n2))
            elif token == "*": 
                stack.append(stack.pop() * stack.pop())
            elif token == "-": 
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1-n2)

            else: stack.append(int(token))
        
        return stack[0]
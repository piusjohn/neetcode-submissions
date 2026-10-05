class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        exp = " ".join(tokens).split()
        stack = []
        for token in exp:
            if token in {'+', '-', '*', '/'}:
                right  = stack.pop()
                left = stack.pop()
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "/":
                    result = int(left / right)
                elif token == "*":
                    result = left * right
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

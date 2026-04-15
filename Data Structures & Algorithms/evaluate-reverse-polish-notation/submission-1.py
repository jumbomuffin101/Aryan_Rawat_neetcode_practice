class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ref = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in ref:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    result = left + right
                    stack.append(result)
                elif token == "-":
                    result = left - right
                    stack.append(result)
                elif token == "*":
                    result = left * right
                    stack.append(result)
                else:
                    result = int (left / right)
                    stack.append(result)
        return stack.pop()
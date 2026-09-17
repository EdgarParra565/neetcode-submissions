class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    a, b = stack.pop(), stack.pop()
                    c = b - a
                    stack.append(c)
                elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    a, b = stack.pop(), stack.pop()
                    c = b / a
                    stack.append(int(c))
        return stack.pop()

         
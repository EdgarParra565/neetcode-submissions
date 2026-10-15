class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subString = ""
                while stack[-1] != "[":
                    subString = stack.pop() + subString
                stack.pop()
                temp = ""
                while stack and stack[-1].isdigit():
                    temp = stack.pop() + temp
                stack.append(subString * int(temp))
        return "".join(stack)
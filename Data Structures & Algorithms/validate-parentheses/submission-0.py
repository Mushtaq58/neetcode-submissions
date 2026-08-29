class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if (stack[-1] == '(' and s[i] == ')') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '[' and s[i] == ']'):
                    stack.pop()
                else: return False

        return not stack # equivalent to if stack is empty
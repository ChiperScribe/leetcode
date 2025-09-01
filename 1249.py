# 1.
# Remove invalid parentheses using a stack
# Mark characters to remove by setting them to an empty string

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s) # convert string to list for easy modification
        stack = [] # store index of '('

        for i, ch in enumerate(chars):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop() # match ')' with '('
                else:
                    chars[i] = "" # remove unmatched ')'

        for i in stack:
            chars[i] = "" # remove unmatched '('

        return "".join(chars) # convert list back to string

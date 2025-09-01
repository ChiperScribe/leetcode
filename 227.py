# 1.
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'  # previous operator
        num = 0  # current number being processed

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)  # build multi-digit number

            # if current char is an operator, or it's the last char
            if ch in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num) # python specialty

                sign = ch
                num = 0

        return sum(stack)

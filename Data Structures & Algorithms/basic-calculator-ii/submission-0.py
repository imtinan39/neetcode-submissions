class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"

        for i in s + '+':  # sentinel '+' forces final flush
            if i.isdigit():
                num = num * 10 + int(i)
            elif i in '+-*/':
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = i
                num = 0

        return sum(stack)
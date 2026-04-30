class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for i in s:
            stack.append(i)
            result = ""
            while stack and i == "]":
                tmp = stack.pop()

                if tmp != "[" and tmp != "]":
                    result = tmp +result

                elif tmp == "[":

                    rang = ""
                    while stack and stack[-1].isdigit():
                        rang = stack.pop() + rang 
        
                    stack.append(result*int(rang))
                    break
        



        return "".join(stack)

        
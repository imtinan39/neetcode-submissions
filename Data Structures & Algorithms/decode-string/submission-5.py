class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        result = ""
        res = []
        for i in s:
            stack.append(i)
            result = ""
            while stack and i == "]":
                tmp = stack.pop()

                if tmp != "[" and tmp != "]":
                    result = tmp +result

                elif tmp == "[":

                    tmp_s = ""
                    rang = ""
                    while stack and stack[-1].isdigit():
                        rang = stack.pop() + rang 
                    for i in range(int(rang)):
                        tmp_s += result
                    stack.append(tmp_s)
        p=""

        for i in range(len(stack)):
            p+=stack[i]



        return p

        
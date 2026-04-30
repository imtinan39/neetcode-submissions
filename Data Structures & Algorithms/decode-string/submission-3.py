class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        result = ""
        res = []
        for i in s:
            stack.append(i)
            result = ""
            print("stack", stack)
            while stack and i == "]":
                tmp = stack.pop()

                if tmp != "[" and tmp != "]":
                    result = tmp +result

                elif tmp == "[":

                    tmp_s = ""
                    rang = stack.pop()
                    while stack and stack[-1].isdigit():
                        rang = stack.pop() + rang  # prepend to preserve order
                    for i in range(int(rang)):
                        tmp_s += result
                    stack.append(tmp_s)
                    print("stack-2", stack)
        p=""

        for i in range(len(stack)):
            p+=stack[i]



        return p

        
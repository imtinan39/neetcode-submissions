from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        count = 0
        k = 0
        tmp = ""

        while read < len(chars):
            if chars[read] == chars[write]:
                read += 1
                count += 1
            else:
                if count == 1:
                    tmp = chars[write]
                else:
                    tmp = chars[write] + str(count)

                count = 0
                for i in tmp:
                    chars[k] = i
                    k += 1
                tmp = ""
                write = read

        if count == 1:
            chars[k] = chars[write]
            k += 1
        else:
            tmp = chars[write] + str(count)
            for i in tmp:
                chars[k] = i
                k += 1

        return k


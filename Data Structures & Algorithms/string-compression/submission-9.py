from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0
        count=0

        while read<len(chars):
            ch=chars[read]

            while read<len(chars) and ch==chars[read]:
                read+=1
                count+=1
            
            chars[write]=ch
            write+=1
            if count>1:
                for d in str(count):
                    chars[write]=d
                    write+=1
            count=0

        return write
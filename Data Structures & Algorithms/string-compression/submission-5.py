class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0
        count=0
        total=0
        k=0
        tmp=""
        while read < len(chars):
            if chars[read]==chars[write]:
                read+=1
                count+=1
            else:
                if count==1:
                    total+=1
                    tmp=chars[write]
                if count>1:
                    tmp= chars[write]+str(count)
                    total+=len(tmp)
                count=0
                for i in tmp:
                    chars[k]=i
                    k+=1
                tmp=""
                write=read

        if count==1:
            total+=1
            chars[k]=chars[write]
            k+=1

        if count>1:
            tmp= chars[write]+str(count)
            total+=len(tmp)
            for i in tmp:
                    chars[k]=i
                    k+=1
        return total



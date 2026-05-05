class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        st=list(s)
        

        count=0


        for i in shift:
            if i[0]==0:
                count=count+i[1]
            else:
                count=count-i[1]
        print(count)
        count = count % len(st)
        if count<0:
            ft=st[count:]+st[:len(st)-abs(count)]
            print(ft)
            stri=""
            for i in ft:
                stri+="".join(i)
            print(stri)
            return stri

        elif count>0:
            ft=st[count:len(st)]+st[:count]
            print(ft)
            stri=""
            for i in ft:
                stri+="".join(i)
            return stri
        else:
            return s


                

        
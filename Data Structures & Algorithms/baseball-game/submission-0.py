class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        def is_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False    

        for i,j in enumerate(operations):
            if is_int(j):
                result.append(int(j))
            elif j=="+":
                print(result[-1]+result[-2])
                result.append(result[-1]+result[-2])
            elif j=="D":
                result.append(result[-1]*2)
            elif j=="C":
                del result[-1]
        suma=0
        print(result)

        for i in result:
            suma+=i
        return suma

        
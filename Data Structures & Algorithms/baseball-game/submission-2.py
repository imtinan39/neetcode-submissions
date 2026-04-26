class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]   

        for i,j in enumerate(operations):
            if j=="+":
                print(result[-1]+result[-2])
                result.append(result[-1]+result[-2])
            elif j=="D":
                result.append(result[-1]*2)
            elif j=="C":
                del result[-1]
            else:
                result.append(int(j))
        
        return sum(result)

        
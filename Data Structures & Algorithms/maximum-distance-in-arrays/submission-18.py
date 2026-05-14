class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxim=-100000000
        max_1=[-100000]*len(arrays)
        max_2=[-100000]*len(arrays)
        max_3=[-100000]*len(arrays)

        max_1[-1]=arrays[-1][-1]
        max_2[0]=arrays[0][-1]

        for i in range(len(arrays)-2,-1,-1):
            max_1[i]=max(max_1[i+1],arrays[i][-1])
        for i in range(1,len(arrays)):
            max_2[i]=max(max_2[i-1],arrays[i][-1])

        max_3[0]=max_1[1]
        max_3[-1]=max_2[-2]
        
        for i in range(1,len(arrays)-1):
            max_3[i]=max(max_2[i-1],max_1[i+1])
        
        for i in range(len(arrays)):
            maxim=max(maxim,abs(max_3[i]-arrays[i][0]))
        

        return maxim
        
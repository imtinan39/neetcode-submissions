class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        hashmap={}

        for i in grid:
            for j in i:
                hashmap[j]=hashmap.get(j,0)+1
        
        n=len(grid)
        ans=[0]*2
        for i in range(1, (n*n)+1):
            if i in hashmap and hashmap[i]==2 :
                ans[0]=i
            elif i not in hashmap:
                ans[1]=i
        return ans

        
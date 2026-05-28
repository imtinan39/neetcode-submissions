class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common=list(set(mat[0]))
        for i in range(1,len(mat)):
            common=list(set(common) & set(mat[i]))
        
        return min(common) if len(common)!=0 else -1
        
      

        
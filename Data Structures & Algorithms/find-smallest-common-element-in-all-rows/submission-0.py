class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common = list(set.intersection(*(set(lst) for lst in mat)))
        return min(common) if len(common)!=0 else -1
        
      

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        col=len(matrix[0])
        left=0
        right=(len(matrix[0])*len(matrix))-1
        while left<=right:
            mid=(left+right)//2
            i=mid//col
            j=mid%col
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                right=mid-1
            else:
                left=mid+1
        return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag=0
        for i in range(len(matrix)):
            left=0
            right=len(matrix[i])-1
            if flag==1:
                return False
            while left<=right:
                mid=(left+right)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    right=mid-1
                    flag=1
                else:
                    left=mid+1
        return False
        
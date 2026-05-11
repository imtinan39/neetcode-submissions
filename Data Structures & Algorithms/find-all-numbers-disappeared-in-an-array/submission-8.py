class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i,j in enumerate(nums):
            if j>0:
                nums[j-1]=abs(nums[j-1])*(-1)
            else:
                nums[abs(j)-1]=abs(nums[abs(j)-1])*(-1)



        return [i+1 for i,j in enumerate(nums)  if j>0]
        
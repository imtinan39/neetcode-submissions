class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r=1
        flag=0
        k=1

        while r<len(nums):
            if nums[r]!=nums[k-1]:
                nums[k]=nums[r]
                k+=1
                r+=1
                flag=0
            elif nums[r]==nums[k-1] and flag==1:
                r+=1
            elif nums[r]==nums[k-1] and flag==0:
                nums[k]=nums[r]
                k+=1
                r+=1
                flag=1
        return k





        
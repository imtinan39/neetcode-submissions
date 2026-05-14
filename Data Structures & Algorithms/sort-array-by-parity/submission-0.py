class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=0
        tmp=None

        while r<len(nums):
            if nums[r]%2==0:
                tmp=nums[l]
                nums[l]=nums[r]
                nums[r]=tmp
                l+=1
                r+=1
            else:
                r+=1
        return nums

        
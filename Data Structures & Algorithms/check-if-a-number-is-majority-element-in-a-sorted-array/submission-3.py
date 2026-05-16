class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        l=0
        r=len(nums)-1
        index=0
        count=0
        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                index=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return index+(len(nums)//2)<len(nums) and nums[index+len(nums)//2]==target



        
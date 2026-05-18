class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            mid=(l+r)//2
            if mid%2!=0:
                mid=mid-1
            
            if nums[mid]==nums[mid+1]:
                l=mid+2
            elif nums[mid]!=nums[mid+1]:
                r=mid
        return nums[r]
        
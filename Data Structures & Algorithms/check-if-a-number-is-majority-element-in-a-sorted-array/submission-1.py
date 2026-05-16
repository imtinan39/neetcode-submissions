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
        for i in range(index,len(nums)):
            if nums[i]==target:
                count+=1
        print(count)
        return count>len(nums)//2



        
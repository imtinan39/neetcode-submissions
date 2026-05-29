class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bls(nums,target):
            le=-1
            l=0
            r=len(nums)-1

            while l<=r:
                mid=(l+r)//2

                if nums[mid]==target:
                    le=mid
                    r=mid-1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return le
        def brs(nums,target):
            ri=-1
            l=0
            r=len(nums)-1

            while l<=r:
                mid=(l+r)//2

                if nums[mid]==target:
                    ri=mid
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return ri
        return [bls(nums,target),brs(nums,target)]
    
        
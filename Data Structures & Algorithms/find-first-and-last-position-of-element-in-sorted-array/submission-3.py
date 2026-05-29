class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans=[-1,-1]
        le=-1
        ri=-1
        def bls(nums,target):
            le=-1
            ri=-1
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
            le=-1
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
        ans[0]=bls(nums,target)
        ans[1]=brs(nums,target)
        return [bls(nums,target),brs(nums,target)]
    
        
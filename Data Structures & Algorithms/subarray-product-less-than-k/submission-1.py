class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        total=1
        if k <= 1:
            return 0

        l=0
        ans=0

        for r in range(len(nums)):
            total*=nums[r]

            while total>=k:
                total//=nums[l]
                l+=1
            if total<k:
                ans+=r - l + 1
        return ans
        
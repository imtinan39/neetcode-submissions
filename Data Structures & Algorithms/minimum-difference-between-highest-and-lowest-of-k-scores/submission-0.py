class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans=float("inf")
        l=0
        nums.sort()

        for r in range(len(nums)):
            if r-l+1==k:
                ans=min(ans,nums[r]-nums[l])
                l+=1
        return ans
        
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        total=0
        ans=0
        result={0:1}

        for i in nums:
            total+=i
            ans+=result.get(total-goal,0)
            result[total]=result.get(total,0)+1
        return ans

        
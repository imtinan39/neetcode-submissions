class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result={0:1}
        count=0
        total=0
        for i in nums:
            total+=i
            if total-k in result:
                count+=result[total-k]
            result[total]=result.get(total,0)+1
        return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result={}
        count=0
        total=0
        result[0]=1
        for i in nums:
            total+=i
            if total-k in result:
                count=count+result[total-k]
            result[total]=result.get(total,0)+1
        return count
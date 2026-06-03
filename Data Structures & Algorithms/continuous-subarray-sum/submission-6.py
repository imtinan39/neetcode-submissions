class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        result={0:-1}
        total=0
        for j,i in enumerate(nums):
            total+=i
            rem=total%k
            if rem in result:
                if j-result[rem]>=2:
                    return True
            if rem not in result:
                result[rem]=j
        return False


        
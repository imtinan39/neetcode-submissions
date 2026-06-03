class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        result={0:-1}
        total=0
        for j,i in enumerate(nums):
            total+=i

            if total%k in result:
                if j-result[total%k]>=2:
                    return True
            if total%k not in result:
                result[total%k]=j
        return False


        
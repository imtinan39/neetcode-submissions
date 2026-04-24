class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comple={}

        for i in range(len(nums)):
            complement=target-nums[i]
            if complement not in comple:
                comple[nums[i]]=i
            else:
                return [comple[complement],i]
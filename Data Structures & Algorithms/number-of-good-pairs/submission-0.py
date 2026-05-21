class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0

        for i, num1 in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num1==nums[j]:
                    count+=1
        return count
        
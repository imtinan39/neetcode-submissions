class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for j in nums:
            idx = abs(j) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, j in enumerate(nums) if j > 0]
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        rang=len(nums)
        for i in range(rang):
            nums.append(nums[i])
        return nums
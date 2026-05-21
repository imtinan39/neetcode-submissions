class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if nums[-1]>=nums[0]:
            for i in range(1,len(nums)):
                if nums[i]>=nums[i-1]:
                    continue
                else:
                    return False
        elif nums[-1]<=nums[0]:
            for i in range(1,len(nums)):
                if nums[i]<=nums[i-1]:
                    continue
                else:
                    return False
        return True

        
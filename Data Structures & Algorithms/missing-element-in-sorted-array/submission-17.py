from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2
            if (nums[mid] - nums[0]) - mid < k:
                left = mid + 1
            else:
                right = mid

        return nums[0] + k + left - 1

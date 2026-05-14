

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = -1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                result = max(result, current_sum)
                left += 1      # try a larger sum
            else:
                right -= 1     # sum too large, shrink it

        return result

        
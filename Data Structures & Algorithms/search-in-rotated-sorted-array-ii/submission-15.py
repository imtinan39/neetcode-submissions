class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return True

            if nums[l] < nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:  # nums[l] <= target < nums[mid]
                    r = mid - 1
            elif nums[l] == nums[mid]:
                l+=1

            # Right half is sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:  # nums[mid] < target <= nums[r]
                    l = mid + 1

        return False


        
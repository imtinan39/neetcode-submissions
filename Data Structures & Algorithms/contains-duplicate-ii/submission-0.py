class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        windows=set()
        l=0
        for r, num in enumerate(nums):
            if num in windows:
                return True
            windows.add(num)            # add FIRST
            if r - l + 1 > k:          # now check size
                windows.remove(nums[l])
                l+= 1
        return False



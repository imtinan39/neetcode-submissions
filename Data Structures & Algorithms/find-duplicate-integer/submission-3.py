class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Step 1: find where slow and fast meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: find the duplicate number
        start = nums[0]
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return slow
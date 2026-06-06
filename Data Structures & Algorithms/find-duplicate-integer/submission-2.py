class Solution:
    def findDuplicate(self, nums):
        # Phase 1: detect cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]           # move 1 step
            fast = nums[nums[fast]]     # move 2 steps
            if slow == fast:
                break

        # Phase 2: find cycle entrance
        ptr1 = nums[0]
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
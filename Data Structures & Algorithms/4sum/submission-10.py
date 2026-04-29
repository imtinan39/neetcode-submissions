class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans_set = {}

        for left_0 in range(n - 3):
            if left_0>0 and nums[left_0]==nums[left_0-1]:
                continue
            for right_0 in range(left_0 + 3, n):
                if right_0<n-2 and nums[right_0]==nums[right_0+1]:
                    continue
                left_1 = left_0 + 1
                right_1 = right_0 - 1

                while left_1 < right_1:
                    total = nums[left_0] + nums[left_1] + nums[right_1] + nums[right_0]

                    if total > target:
                        right_1 -= 1
                    elif total < target:
                        left_1 += 1
                    else:
                        ans = [nums[left_0], nums[left_1], nums[right_1], nums[right_0]]
                        ans_set[tuple(ans)] = 1
                        left_1 += 1
                        right_1 -= 1

        answer = [list(key) for key in ans_set.keys()]
        return answer

        
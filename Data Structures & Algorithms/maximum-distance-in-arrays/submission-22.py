class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]

        for i in range(1, len(arrays)):
            arr = arrays[i]

            res = max(res, abs(arr[-1] - cur_min), abs(cur_max - arr[0]))

            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        return res

from bisect import bisect_right
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        positions = defaultdict(list)
        for i, ch in enumerate(source):
            positions[ch].append(i)

        for ch in target:
            if ch not in positions:
                return -1

        count = 1
        curr_pos = -1

        for ch in target:
            idx_list = positions[ch]
            next_idx = bisect_right(idx_list, curr_pos)

            if next_idx == len(idx_list):
                count += 1
                curr_pos = idx_list[0]
            else:
                curr_pos = idx_list[next_idx]

        return count


class Solution:
    def maxDifference(self, s: str) -> int:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        max_odd = 0
        min_even = float('inf')

        for freq in count:
            if freq == 0:
                continue
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even


        
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def requireday(n):
            count = 1
            s = 0
            for i in weights:
                if s + i <= n:
                    s += i
                else:
                    s = i
                    count += 1
            return count

        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l + r) // 2
            need = requireday(mid)
            if need > days:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
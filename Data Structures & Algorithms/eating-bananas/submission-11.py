class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_required(k):
            return sum((p+k-1)// k for p in piles)
        
        index = None
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if hours_required(mid) <= h:
                index=mid
                right = mid - 1
            else:
                left = mid + 1
        
        return left
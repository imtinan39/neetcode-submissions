class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def requireday(n):
            count = 0
            s = 0
            for i in weights:
                if s + i <= n:
                    s += i
                else:
                    s = 0
                    s += i
                    count += 1
            if s<=n:
                count+=1
            return count

        l=max(weights)
        r=sum(weights)
        index=None
        while l<=r:
            mid=(l+r)//2
            need=requireday(mid)
            if need>days:
                l=mid+1
            elif need<days:
                r=mid-1
            else:
                r=mid-1
        
        return l
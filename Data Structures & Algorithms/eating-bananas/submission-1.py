class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        def hourRequire(n):
            count=0
            for i in piles:
                if i<n:
                    count+=1
                elif i==n:
                    count+=1
                else:
                    count=count+math.ceil(i/n)
            return count
        index=None
        left=1
        right=piles[-1]
        while left<=right:
            mid=(left+right)//2
            if hourRequire(mid)==h:
                index=mid
                right=mid-1
            elif hourRequire(mid)>h:
                left=mid+1
            else:
                index=mid
                right=mid-1
                

        return index

        
class Solution:
    def arrangeCoins(self, n: int) -> int:

        def gauss(n):
            return (n*(n+1))//2
        l=1
        r=n
        g=1
        while l<=r:
            mid=(l+r)//2

            if gauss(mid)==n:
                g=mid
                return g
            elif gauss(mid)>n:
                r=mid-1
            else:
                g=max(g,mid)
                l=mid+1
                
        return g
        
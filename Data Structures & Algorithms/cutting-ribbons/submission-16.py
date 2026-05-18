class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        def helper(n):
            total=0
            for i in ribbons:
                total+=(i//n)
            return total
        

        l=1
        r=max(ribbons)
        ans=0
        while l<=r:
            mid=(l+r)//2

            if helper(mid)==k:
                ans=max(ans,mid)
                l=mid+1
            elif helper(mid)>k:
                print(helper(mid),"--",mid)
                ans=max(ans,mid)
                l=mid+1
            else:
                print(helper(mid),"-------",mid)
                r=mid-1
        
        return ans
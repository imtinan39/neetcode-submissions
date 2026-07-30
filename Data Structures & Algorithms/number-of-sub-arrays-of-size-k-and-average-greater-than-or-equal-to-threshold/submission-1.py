class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l=0

        ans=0
        total=0

        for r,n in enumerate(arr):
            total+=n
            if r-l+1==k and total/k>=threshold:
                ans+=1
                total-=arr[l]
                l+=1
            elif r-l+1==k and total/k<threshold:
                total-=arr[l]
                l+=1
        return ans







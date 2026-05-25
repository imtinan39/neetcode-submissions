class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        ans=0
        total=0

        for r in range(len(arr)):

            total+=arr[r]

            if r-l+1==k:
                if (total)/k>=threshold:
                    ans+=1
                
                total-=arr[l]
                l+=1
        return ans


        
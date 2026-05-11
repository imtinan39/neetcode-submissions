class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[0]*(len(nums)+1)
        
        for i in nums:
            ans[i]=1
        
        return [ i for i in range(1,len(ans)) if ans[i]==0]

        
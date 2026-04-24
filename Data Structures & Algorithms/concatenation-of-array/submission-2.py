class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*2*len(nums)
        print(ans)
        k=0
        for i in range(2):
            for j in range(len(nums)):
                ans[k]=nums[j]
                k+=1
        return ans
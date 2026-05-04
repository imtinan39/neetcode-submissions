class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count=[0]*1001
        maxi=-1

        for i in nums:
            count[i]+=1
            maxi=max(maxi,i)

        while maxi>=0:
            if count[maxi]==1:
                return maxi
            else:
                maxi-=1
        return -1
        
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        trac=[]
        trac.append(0)
        maxi=0

        for i in range(len(nums)):
            if nums[i]>trac[-1] and nums[i]<k:
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]<k:
                        maxi=max(maxi,(nums[i]+nums[j]))
                trac.append(nums[i])
        
        if maxi==0:
            return -1
        else:
            return maxi
        
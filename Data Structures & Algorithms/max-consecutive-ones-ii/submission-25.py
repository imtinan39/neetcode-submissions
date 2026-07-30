class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=0
        l=0
        dic={}
        count=0
        for r,n in enumerate(nums):
            dic[n]=dic.get(n,0)+1
            if n==0:
                count+=1
            while dic.get(0, 0)>1:
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                    count=0
                l+=1
            length=max(length,r-l+1)
        return length





        
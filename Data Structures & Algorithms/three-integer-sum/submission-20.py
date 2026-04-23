class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorting keeps the duplicate together and make the skipping easier
        result=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue #avoiding same duplicate
            while l<r:
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l <r and nums[l]==nums[l+1]:
                            l+=1 #avoiding same duplicate
                    l+=1 # go past last duplicate
                    while r>l and nums[r]==nums[r-1]:
                            r-=1 # avoiding same duplicate
                    r-=1 # go ahead last duplicate
            
        return result



        
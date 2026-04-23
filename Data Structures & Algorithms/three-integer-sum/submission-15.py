class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

        result = list(set(tuple(x) for x in result))
        result = [list(x) for x in result]
        return result



        
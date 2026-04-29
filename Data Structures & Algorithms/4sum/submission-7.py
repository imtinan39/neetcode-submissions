class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        left_0=0
        right_0=len(nums)-1
        ans_set={}

        for left_0 in range(len(nums)):
            for right_0 in range(len(nums)):
                left_1=left_0+1
                right_1=right_0-1
                while left_1<right_1:
                    if nums[left_0]+nums[left_1]+nums[right_0]+nums[right_1]>target:
                       
                        right_1-=1
                    elif nums[left_0]+nums[left_1]+nums[right_0]+nums[right_1]<target:
                    
                        left_1+=1
                    else:
                        ans=[nums[left_0],nums[left_1],nums[right_0],nums[right_1]]
                        ans.sort()
                        ans_set[tuple(ans)]=1
                        left_1+=1
                        right_1-=1
                
    
        answer=[ list(key) for key in ans_set.keys()]
        print(answer)

        return answer
                

        
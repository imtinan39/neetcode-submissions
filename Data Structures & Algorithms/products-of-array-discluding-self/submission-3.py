class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        premul=[]
        lastmul={}
        output=[]
        total=1
        total2=1

        for i in range(len(nums)):
            total*=nums[i]
            premul.append(total)
        for i in range(len(nums)-1,-1,-1):
            total2*=nums[i]
            lastmul[i]=total2
        for j in range(len(nums)):
            if j==0:
                output.append(lastmul[j+1])
            elif j==len(nums)-1:
                output.append(premul[j-1])
            else:
                output.append(premul[j-1]*lastmul[j+1])
        return output



        
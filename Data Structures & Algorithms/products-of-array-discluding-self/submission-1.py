class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixmul=[]
        backfixmul={}
        total1=1
        total2=1
        j=len(nums)-1
        result=[]
        for i in range(len(nums)):
            total1*=nums[i]
            prefixmul.append(total1)
        while j>=0:
            total2*=nums[j]
            backfixmul[j]=total2
            j=j-1
        print(backfixmul)
            
        for i in range(len(nums)):
            if i==0:
                result.append(backfixmul[i+1])
            elif i==len(nums)-1:
                result.append(prefixmul[i-1])
            else:
                result.append(prefixmul[i-1]*backfixmul[i+1])
        return result




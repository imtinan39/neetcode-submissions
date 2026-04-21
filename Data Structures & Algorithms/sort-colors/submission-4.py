class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        two=0
        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            elif i==2:
                two+=1

        for i in range(0,zero):
            nums[i]=0
        for j in range(zero, zero+one):
            nums[j]=1
        for k in range(zero+one,zero+one+two):
            nums[k]=2
        print(nums)
        
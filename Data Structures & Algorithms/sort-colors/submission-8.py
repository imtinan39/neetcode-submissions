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
        nums[0:zero]= [0] * zero
        nums[zero:zero+one]=[1] * one
        nums[zero+one:zero+one+two]=[2] * two
        print(nums)
        
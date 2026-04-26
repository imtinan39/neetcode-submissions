class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        for i in range(k):
            tmp=nums[-1]
            for j in range(len(nums)-1,-1,-1):
                if j==0:
                    nums[j]=tmp
                else:
                    nums[j]=nums[j-1]

        
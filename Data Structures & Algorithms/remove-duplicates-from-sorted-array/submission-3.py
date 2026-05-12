class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        else:
            write=0
            for i in range(1,len(nums)):
                if nums[i]!=nums[write]:
                    write+=1
                    nums[write]=nums[i]
            return write+1
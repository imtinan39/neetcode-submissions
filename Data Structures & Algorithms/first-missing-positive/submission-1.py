class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length=0
        
        while 1+length>0:
            if 1+length in nums:
                length+=1
                continue
            else:
                length+=1
                return length
                brreak
        
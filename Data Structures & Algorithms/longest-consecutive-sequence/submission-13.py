class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        li=set(nums)
        longest=0
        for i in li:
            if i-1 not in li:
                length=0
                while i+length in li:
                    length+=1
                    longest=max(length,longest)
        return longest


        
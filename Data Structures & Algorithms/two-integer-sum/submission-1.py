class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countmap={}
        result=[]
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in countmap:
                result.append(countmap[complement])
                result.append(i)
            else:
                countmap[nums[i]]=i
        return sorted(result)
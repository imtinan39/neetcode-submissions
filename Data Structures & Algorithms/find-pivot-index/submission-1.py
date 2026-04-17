class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index=-1
        presum=[]
        total=0
        for i in nums:
            total+=i
            presum.append(total)
        for i in range(len(nums)):
            if i==0:
                leftsum=0
                rightsum=presum[len(nums)-1]-presum[0]
                if leftsum==rightsum:
                    index=i
                    return index
            elif i==len(nums)-1:
                rightsum=0
                leftsum=presum[i-1]
                if leftsum==rightsum:
                    index=i
                    return index
            else:
                leftsum=presum[i-1]
                rightsum=presum[len(nums)-1]-presum[i]
                if leftsum==rightsum:
                    index=i
                    return index
        return index


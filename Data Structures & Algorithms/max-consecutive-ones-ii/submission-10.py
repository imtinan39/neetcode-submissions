class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=0
        l=0
        dq=deque(maxlen=2)
        for r in range(len(nums)):

            if nums[r]==0:
                dq.append(r)
            
            if len(dq)==2:
                length=max(r-l,length)
                l=dq.popleft()+1
            length=max(r-l+1,length)
        return length





        
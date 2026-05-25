class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flag=0
        length=0
        l=0
        dq=deque(maxlen=2)
        for r in range(len(nums)):

            if nums[r]==0:
                flag+=1
                dq.append(r)
                if flag==1 or flag==0:
                    length=max(r-l+1,length)

            
            if flag==2:
                length=max(r-l,length)
                flag-=1
                l=dq[0]+1
            length=max(r-l+1,length)
        return length





        
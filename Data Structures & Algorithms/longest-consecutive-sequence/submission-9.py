class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictd={}
        for i in nums:
            dictd[i]=dictd.get(i,0)+1
        
        count=1
        answer=0
        li=[]
        for i in dictd.keys():
            li.append(i)
        li.sort()
        if len(li)==0:
            return 0
        elif len(li)==1:
            return 1
        for i in range(1,len(li)):
            if li[i-1]==li[i]-1:
                count+=1
                answer=max(answer,count)
            else:
                answer=max(answer,count)
                count=1
        return answer


        
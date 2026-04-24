class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length=0
        dictd={}
        for i in nums:
            if i>=0:
                dictd[i]=dictd.get(i,0)+1
        while 1+length>0:
            if dictd.get(1 + length, 0) >= 1:
                length+=1
            else:
                length+=1
                return length
        
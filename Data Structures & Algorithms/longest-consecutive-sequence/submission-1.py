class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            dicts[i]=dicts.get(i,0)+1
        li=[]
        for i in dicts.keys():
            li.append(i)
        count=0  
        answer=0

        for i in li:
            if i in dicts:
                count+=1
                j=i+1
                while count>0:
                    if j in dicts:
                        count+=1
                        j+=1
                    else:
                        answer=max(answer,count)
                        count=0
                        break
        return answer

        
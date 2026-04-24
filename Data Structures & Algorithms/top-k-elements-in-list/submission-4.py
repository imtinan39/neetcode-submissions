class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq=[[] for i in range(len(nums)+1)]
        dic={}
        result=[]

        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in dic.keys():
            freq[dic[i]].append(i)
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                result.append(j)
                if len(result)==k:
                    return result
        
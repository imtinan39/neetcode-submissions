class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        ans=set()

        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i in nums:
            if hashmap[i]>len(nums)/3:
                ans.add(i)
        return list(ans)

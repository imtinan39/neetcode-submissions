class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        result=set()
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
            if hashmap[i]> len(nums)/3:
                result.add(i)
        
        return list(result)
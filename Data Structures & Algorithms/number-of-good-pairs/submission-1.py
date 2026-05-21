class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0

        hashmap={}

        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        
        for i in hashmap.values():

            count+= (i*(i-1))//2

        return count
        
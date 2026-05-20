class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap={}

        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i in hashmap.keys():
            if hashmap[i]%2==0:
                continue
            else:
                return False
        return True
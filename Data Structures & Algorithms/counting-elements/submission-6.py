class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashmap={}
        for i in arr:
            hashmap[i]=1
        count=0

        for i in arr:
            if i+1 in hashmap:
                count+=1
        return count
        
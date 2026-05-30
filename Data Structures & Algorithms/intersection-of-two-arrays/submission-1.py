class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap={}

        for i in nums1:
            hashmap[i]=hashmap.get(i,0)+1
        
        ans=[]

        for j in nums2:
            if j in hashmap:
                ans.append(j)
        return list(set(ans))
        
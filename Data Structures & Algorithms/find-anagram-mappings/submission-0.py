class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        for i,j in enumerate(nums2):
            hashmap[j]=i
            print(i,j)

        return [hashmap[k] for k in nums1]

        
        
        
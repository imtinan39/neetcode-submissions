class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashmap_2={}
        hashmap_1={}

        for i in nums1:
            hashmap_1[i]=1
        for i in nums2:
            hashmap_2[i]=1
        ans=[]
        ans_1=[]
        

        for i in hashmap_1.keys():
            if i not in hashmap_2:
                ans.append(i)
        for i in hashmap_2.keys():
            if i not in hashmap_1:
                ans_1.append(i)

        return [ans,ans_1]
    

        
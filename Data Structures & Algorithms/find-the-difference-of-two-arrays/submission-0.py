class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashmap_2={}
        hashmap_1={}

        for i in nums1:
            hashmap_1[i]=1
        for i in nums2:
            hashmap_2[i]=1
        answer=[]
        ans=[]
        ans_1=[]
        

        for i in set(nums1):
            if i not in hashmap_2:
                ans.append(i)
        answer.append(ans)
        for i in set(nums2):
            if i not in hashmap_1:
                ans_1.append(i)
        answer.append(ans_1)
        return answer
    

        
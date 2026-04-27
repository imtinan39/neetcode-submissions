class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result=[-1]*len(nums1)
        hashmap={}
        stack=[]
        
        for i, num in enumerate(nums2):
            while stack and num>stack[-1]:
                hashmap[stack.pop()]=num
            stack.append(num)
        
        for i,j in enumerate(nums1):
            if j in hashmap:
                result[i]=hashmap[j]
        return result

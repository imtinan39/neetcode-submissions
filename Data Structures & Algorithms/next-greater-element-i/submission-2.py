class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result=[-1]*len(nums1)
        hashmap={}
        stack=[]
        
        for i, num in enumerate(nums2):
            while stack and num>stack[-1]:
                hashmap[stack.pop()]=num
            stack.append(num)
        
        return [hashmap.get(num, -1) for num in nums1]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap={}
        ans=[]
        for i in nums:
            hashmap[i]=True
        
        for i in range(1,len(nums)+1):
            if i not in hashmap:
                ans.append(i)
        return ans

        
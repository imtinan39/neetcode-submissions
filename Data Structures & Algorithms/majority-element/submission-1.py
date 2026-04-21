class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictd={}
        for i in nums:
            dictd[i]=dictd.get(i,0)+1

        for i in dictd.keys():
            print(i)
            if dictd[i]> len(nums)//2:
                return i


class NumArray:

    def __init__(self, nums: List[int]):
        self.presum=[]
        total=0
        for i in nums:
            total+=i
            self.presum.append(total)
        

    def sumRange(self, left: int, right: int) -> int:

        self.result=0
        self.rightsum=self.presum[right]
        if left >0:
            self.leftsum=self.presum[left-1]
        else:
            self.leftsum=0
        self.result=self.rightsum-self.leftsum
        return self.result


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
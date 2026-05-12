class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        print(ans)

        l=0
        r=len(nums)-1
        pos=len(nums)-1
        while l<=r and pos>=0:
            if abs(nums[r])>=abs(nums[l]):

                ans[pos]=nums[r]*nums[r]
                r-=1
                pos-=1
                print(pos)
            else:
                ans[pos]=nums[l]*nums[l]
                l+=1
                pos-=1
                print(pos)

        return ans
        
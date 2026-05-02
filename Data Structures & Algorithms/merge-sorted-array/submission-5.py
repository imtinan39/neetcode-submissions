class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last=len(nums1)-1

        r=m-1
        l=n-1

        while r>=0 and l>=0:

            if nums1[r]>nums2[l]:
                nums1[last]=nums1[r]
                r-=1
            else:
                nums1[last]=nums2[l]
                l-=1
            last-=1
        while l>=0:
            nums1[last]=nums2[l]
            l-=1
            last-=1

        
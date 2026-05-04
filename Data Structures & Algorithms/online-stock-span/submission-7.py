class StockSpanner:

    def __init__(self):
        self.nums = []

    def next(self, price: int) -> int:
        self.nums.append(price)
        nums2 = self.nums[::-1]
        stack = []
        result = [len(nums2)] * len(nums2)

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                result[stack.pop()] = i
            stack.append(i)

        return result[0]
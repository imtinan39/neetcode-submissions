
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 0
        right = x

        while right - left > 0.001:
            mid = (right + left) / 2
            if mid * mid > x:
                right = mid
            else:
                left = mid

        result = int((right + left) / 2)
        if (result + 1) * (result + 1) <= x:
            return result + 1
        return result
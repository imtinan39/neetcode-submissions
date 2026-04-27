class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # indices of surviving positive asteroids

        for i, asteroid in enumerate(asteroids):
            if asteroid > 0:
                stack.append(i)
            else:
                while stack:
                    left = asteroids[i]          # current negative asteroid
                    right = asteroids[stack[-1]] # latest surviving positive asteroid

                    if abs(left) == abs(right):
                        asteroids[i] = 0
                        asteroids[stack.pop()] = 0
                        break
                    elif abs(left) < abs(right):
                        asteroids[i] = 0
                        break
                    else:
                        asteroids[stack.pop()] = 0

        return [asteroid for asteroid in asteroids if asteroid != 0]
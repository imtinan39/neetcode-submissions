from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.w = size
        self.queue = deque()      # stores at most `size` elements
        self.running_sum = 0      # maintained incrementally

    def next(self, val: int) -> float:
        if len(self.queue) == self.w:
            self.running_sum -= self.queue.popleft()

        self.queue.append(val)
        self.running_sum += val

        return self.running_sum / len(self.queue)


# ---------- Example usage ----------
# obj = MovingAverage(3)
# print(obj.next(1))   # 1.0
# print(obj.next(10))  # 5.5
# print(obj.next(3))   # 4.666...
# print(obj.next(5))   # 6.0  → window is [10, 3, 5]

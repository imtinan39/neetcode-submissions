class MovingAverage:

    def __init__(self, size: int):
        self.w = size
        self.queue = deque()      # stores at most `size` elements
        self.running_sum = 0      # maintained incrementally

    def next(self, val: int) -> float:
        # If the window is full, evict the oldest element
        if len(self.queue) == self.w:
            self.running_sum -= self.queue.popleft()

        self.queue.append(val)
        self.running_sum += val

        return self.running_sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

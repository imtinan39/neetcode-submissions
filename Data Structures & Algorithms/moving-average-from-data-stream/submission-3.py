class MovingAverage:

    def __init__(self, size: int):
        self.w = size
        self.queue = deque(maxlen=size)      # stores at most `size` elements
        self.running_sum = 0      # maintained incrementally

    def next(self, val: int) -> float:
        # If the window is full, evict the oldest element

        self.queue.append(val)

        return sum(self.queue) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

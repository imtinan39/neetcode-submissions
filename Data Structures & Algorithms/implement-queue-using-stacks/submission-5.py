class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Always push to the 'in' stack
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has the oldest elements
        self.ask=self.peek()
        self.stack_out.pop()
        return self.ask

    def peek(self) -> int:
        # If stack_out is empty, pour everything from stack_in to stack_out.
        # This reverses the order, putting the oldest elements at the top.
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
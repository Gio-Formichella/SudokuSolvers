class Queue:
    def __init__(self):
        self.queue = []

    def pop(self) -> tuple:
        return self.queue.pop(0)

    def push(self, t: tuple) -> None:
        self.queue.append(t)

    def is_empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

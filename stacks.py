class Stack: # classname
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item: {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
s = Stack() # s is object 
s.push(1)
s.push(2)
s.push(3)
print(f"Popped item: {s.pop()}")
print(f"Top item: {s.peek()}")
print(f"Stack size: {s.size()}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None 
        self._size = 0    

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_value = self.head.data
        self.head = self.head.next
        self._size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

def process_stack_operations(n, operations):
    stack = Stack()

    for operation in operations:
        op = operation.split()
        if op[0] == 'push':
            stack.push(int(op[1]))
        elif op[0] == 'pop':
            print(stack.pop())
        elif op[0] == 'peek':
            print(stack.peek())
        elif op[0] == 'isEmpty':
            print(stack.is_empty())
        elif op[0] == 'size':
            print(stack.size())

if __name__ == "__main__":
    n = int(input())
    operations = [input() for _ in range(n)]
    process_stack_operations(n, operations)


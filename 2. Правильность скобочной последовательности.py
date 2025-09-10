class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)

def bracket_sequence_control(sequence):
    stack = Stack()
    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in sequence:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.peek() != bracket_pairs[char]:
                return False
            stack.pop()

    return stack.is_empty()

def main():
    while True:
        sequence = input("Введите скобочную последовательность: ")

        if bracket_sequence_control(sequence):
            print(f"'{sequence}' - ПРАВИЛЬНАЯ скобочная последовательность")
        else:
            print(f"'{sequence}' - НЕПРАВИЛЬНАЯ скобочная последовательность")

if __name__ == "__main__":
    main()
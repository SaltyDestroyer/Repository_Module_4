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

def evaluate_rpn(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(float(token))
        else:
            if stack.size() < 2:
                raise ValueError("Недостаточно операндов для операции")

            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ZeroDivisionError("Деление на ноль недопустимо")
                result = operand1 / operand2
            else:
                raise ValueError(f"Неизвестный оператор: {token}")

            stack.push(result)

    if stack.size() != 1:
        raise ValueError("Некорректное выражение")

    return stack.pop()

if __name__ == "__main__":
    expression1 = "3 4 2 * +"
    result1 = evaluate_rpn(expression1)
    print(result1)
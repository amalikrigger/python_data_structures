from stack import Stack

def is_balanced(expression):
    stack = Stack()
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening = set(bracket_map.values())
    closing = set(bracket_map.keys())
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if not stack or stack.peek() != bracket_map[char]:
                return False
            stack.pop()
    return not stack

def reverse_string(text):
    stack = Stack()
    reversed_text = ''
    for char in text:
        stack.push(char)
    while stack:
        reversed_text += stack.pop()
    return reversed_text

def evaluate_postfix(expression):
    operands = Stack()
    for token in expression:
        if token.isdigit():
            operands.push(int(token))
        else:
            b = operands.pop()
            a = operands.pop()
            if token == "+":
                operands.push(a + b)
            elif token == "-":
                operands.push(a - b)
            elif token == "*":
                operands.push(a * b)
            elif token == "/":
                operands.push(a / b)
    return operands.pop()
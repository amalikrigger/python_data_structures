from curses.ascii import isdigit

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

# print(reverse_string("hello"))       # "olleh"
# print(reverse_string("Python"))      # "nohtyP"
# print(reverse_string(""))            # ""
# print(reverse_string("racecar"))     # "racecar" (same!)

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


print(evaluate_postfix(["2", "3", "+", "4", "*"]))
print(evaluate_postfix(["2", "3", "+", "4", "*"]))   # 20
print(evaluate_postfix(["5", "1", "2", "+", "4", "*", "+", "3", "-"])) # 14


# def is_balanced(expression):
#     stack = Stack()
#     brackets = {'(': ')', '[': ']', '{': '}'}
#     for i in range(len(expression)):
#         if expression[i] in '([{':
#             stack.push(expression[i])
#         elif brackets[stack.pop()] != expression[i]:
#             return False
#     return stack.is_empty()

# test_cases = [
#     # ✅ Basic valid pairs
#     ("()", True),
#     ("[]", True),
#     ("{}", True),
#
#     # ✅ Nested and mixed valid cases
#     ("([{}])", True),
#     ("{[()()]}", True),
#     ("(([]))", True),
#     ("{([])}", True),
#
#     # ❌ Mismatched types
#     ("(]", False),
#     ("[)", False),
#     ("{]", False),
#     ("[({)]}", False),
#
#     # ❌ Unbalanced brackets
#     ("(((", False),
#     ("[[[", False),
#     ("{{{", False),
#     (")))", False),
#     ("}}}", False),
#     ("]]]", False),
#     ("({[)]}", False),
#
#     # ❌ Closing first
#     (")(", False),
#     ("}[", False),
#     ("]()", False),
#
#     # ✅ Edge cases
#     ("", True),                        # Empty string is trivially balanced
#     ("(((((((((())))))))))", True),   # Deeply nested
#     ("(((((((((()))))))))))", False), # One extra close
#     ("()()()()()()", True),           # Sequential flat structure
#
#     # ✅ Including non-bracket characters (should ignore if allowed)
#     ("a + (b * c) - {d / e}", True),
#     ("[a + b] * (c - d)", True),
#     ("[({a + b}) - c]", True),
#
#     # ❌ Non-bracket chars with imbalance
#     ("[a + b * (c - d}", False),
#
#     # ✅ Whitespace and newline tolerance
#     ("[\n(\t{ \n}) ]", True),
#
#     # ❌ Realistic developer typos
#     ("function(x) { return [1, 2, 3];", False),
#     ("{ [ ( ) ]", False),
#     ("{ [ ( ] ) }", False),
#     ("([{}])]", False),
#     ("([{}])}", False),
#
#     # ✅ Large balanced structure (performance test)
#     ("()" * 10000, True),
#     ("(" * 10000 + ")" * 9999, False)
# ]
#
# for expr, expected in test_cases:
#     print(f"{expr:10} → {is_balanced(expr)} (Expected: {expected})")
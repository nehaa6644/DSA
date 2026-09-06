def is_valid_parentheses(s):
    stack = []

    for bracket in s:

        if bracket == '(':
            stack.append(')')

        elif bracket == '{':
            stack.append('}')

        elif bracket == '[':
            stack.append(']')

        else:
            if not stack or stack.pop() != bracket:
                return False

    return not stack

s = input(" Enter parentheses ")

print(is_valid_parentheses(s))
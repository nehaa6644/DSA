
def evalRPN(tokens):
    stack = []

    for token in tokens:

        # If it is a number
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))

        else:
            # Take the last two numbers
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            elif token == "/":
                result = int(a / b)   # truncates toward zero

            # Put result back into stack
            stack.append(result)

    return stack[0]


# Already given input
tokens = ["2", "1", "+", "3", "*"]

print(evalRPN(tokens))


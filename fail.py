open_to_close = {'{': '}', '[': ']', '(': ')'}
close_to_open = {v: k for k, v in open_to_close.items()}

text = input()

stack = []
for i, char in enumerate(text, 1):
    if char in open_to_close:
        stack.append((i, char))
    elif len(stack):
        _, open_bucket = stack.pop()
        if open_bucket != close_to_open[char]:
            print(i)
            break
    else:
        print(i)
        break
else:
    if stack:
        print(stack[0][0])
    else:
        print("succses")


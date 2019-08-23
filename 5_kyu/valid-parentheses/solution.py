def valid_parentheses(string):
    if len(string) == 0:
        return True
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            try:
                stack.pop()
            except:
                print(stack)
                return False
    print(stack)
    if len(stack) == 0:
        return True
    else:
        return False
def isValid(s):
    stack, match = [], {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in match:
            if not (stack and stack.pop() == match[ch]):
                return False
        else:
            stack.append(ch)
    return not stack

print(isValid("((()(())))"))
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        
        if i in [')', '}', ']']:
            if not stack or mapping[i] != stack.pop():
                return False

    return len(stack) == 0
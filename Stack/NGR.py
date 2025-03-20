# Nearest Greater to Right

from collections import deque


nums = [9,4,6,8,10,3]

def NGR(arr):
    stack = deque() 
    result = []
    for i in reversed(arr):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) != 0 and stack[-1] > i:
            result.append(stack[-1])
        elif len(stack) != 0 and stack[-1] <= i:
            while len(stack) > 0 and stack[-1] <= i:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(i)

    result.reverse()
    return result

print(NGR(nums))
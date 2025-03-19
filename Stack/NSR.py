# Nearest smallest to right

nums = [4,5,2,10,8]


def NSR(arr):
    stack = []
    result = []
    for i in reversed(arr):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) != 0 and stack[-1] < i:
            result.append(stack[-1])
        elif len(stack) != 0 and stack[-1]  >= i:
            while len(stack) > 0 and stack[-1] >= i:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(i)
    
    result.reverse()
    return result


print(NSR(nums))
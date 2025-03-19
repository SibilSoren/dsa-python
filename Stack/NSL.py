# Nearest smallest to left

nums = [4,5,2,10,8]

def NSL(arr):
    stack = []
    result = []
    for i in arr:
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) != 0 and stack[-1] < i:
            result.append(stack[-1])
        elif len(stack) != 0 and stack[-1] > i:
            while len(stack) > 0 and stack[-1] > i:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(i)
    return result

print(NSL(nums))